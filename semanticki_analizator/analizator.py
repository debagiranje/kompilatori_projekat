from sintaksni_analizator.RubyParserListener import RubyParserListener
from .TabelaSimbola import * 


class Analizator(RubyParserListener):
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope
        self.current_class = None
        self.errors = []
        self.global_methods = {}
        self.global_methods = {
            "puts": MethodSymbol("puts", ["arg"]),
            "print": MethodSymbol("print", ["arg"]),
            "gets": MethodSymbol("gets", []),
            # note, ovo nije neko rjesenje, ali ovako cemo prevazici nedostatak importa modula
            # neko moze kasnije da doda opciju za module i sl.
        }

    def enterClass_definition(self, ctx):
        class_name = ctx.klasa.getText()
        superclass_name = ctx.nadklasa.getText() if ctx.nadklasa else None

        if self.current_scope.resolve_class(class_name):
            self.errors.append(f"Err @ [Line {ctx.start.line}] Duplikat klase: {class_name}")
            self.current_class = None
            return

        new_class = ClassSymbol(class_name, superclass_name)
        self.current_scope.define_class(new_class)
        self.current_class = new_class

    def exitClass_definition(self, ctx):
        self.current_class = None

    def enterMethod_definition(self, ctx):
        header = ctx.method_definition_header()
        method_name = header.method_name().getText()

        # parametri metode
        param_list_ctx = header.method_definition_params()
        param_names = []

        if param_list_ctx and param_list_ctx.method_definition_params_list():
            
            def extract_param_ids(pctx):
                if pctx.method_definition_params_list():
                    extract_param_ids(pctx.method_definition_params_list())
                if pctx.method_definition_param_id():
                    param_names.append(pctx.method_definition_param_id().getText())

            
            extract_param_ids(param_list_ctx.method_definition_params_list())
        
        #print(param_names)

        # detekcija duplikata parametara u metodama
        seen = set()
        for name in param_names:
            if name in seen:
                self.errors.append(f"Err @ [Line {ctx.start.line}] Duplikat parametra '{name}' u metodi '{method_name}'")
            seen.add(name)

        method_symbol = MethodSymbol(method_name, param_names)

        if self.current_class:
            if method_name in self.current_class.methods:
                self.errors.append(f"Warning @ [Line {ctx.start.line}] Duplikat metode '{method_name}' u klasi '{self.current_class.name}'.")
            else:
                self.current_class.define_method(method_name, method_symbol)
        else:
            if method_name in self.global_methods:
                self.errors.append(f"Warning @ [Line {ctx.start.line}]: Duplikat globalne metode '{method_name}'.")
            else:
                self.global_methods[method_name] = method_symbol

    def enterMethod_call(self, ctx):

        method_name = None

        actual_params = []

        # standard notacija metode
        if ctx.method_name():
            if isinstance(ctx.method_name(), list):
                method_name = ctx.method_name()[0].getText()
            else:
                method_name = ctx.method_name().getText()
        elif ctx.primary():
            # object dot method call
            if ctx.getChildCount() >= 3:
                method_name = ctx.getChild(2).getText()

        if not method_name:
            self.errors.append(f"Err @ [Line {ctx.start.line}] nemoguce prepoznati naziv metode")
            return


        param_list_ctx_list = ctx.method_call_param_list()
        
        #zagradafull
        if param_list_ctx_list:
            param_list_ctx = param_list_ctx_list[0] if isinstance(param_list_ctx_list, list) else param_list_ctx_list
            method_call_params_ctx = param_list_ctx.method_call_params() if param_list_ctx else None

            if method_call_params_ctx:
                params = method_call_params_ctx.method_param()
                if isinstance(params, list):
                    actual_params = [p.getText() for p in params]
                elif params:
                    actual_params = [params.getText()]


        # zagradaless poziv
        elif ctx.method_call_args():
            args_ctx = ctx.method_call_args()
            params = args_ctx.method_param()
            if isinstance(params, list):
                actual_params = [p.getText() for p in params]
            elif params:
                actual_params = [params.getText()]

        # no args -- param prazni

        # provjera metoda u klasam
        found = False
        search_class = self.current_class
        while search_class:
            method_symbol = search_class.methods.get(method_name)
            if method_symbol:
                found = True
                expected_arity = method_symbol.arity()
                if len(actual_params) != expected_arity:
                    self.errors.append(
                        f"Err @ [Line {ctx.start.line}] poziv metode '{method_name}' sa {len(actual_params)} arg, ocekivano {expected_arity} u klasi '{search_class.name}'"
                    )
                break
            # idi na nadklasu ako postoji
            if search_class.superclass:
                search_class = self.global_scope.resolve_class(search_class.superclass)
            else:
                break

        if not found:
            # provjeri postoji li u globalnim metodama
            if method_name in self.global_methods:
                expected_arity = self.global_methods[method_name].arity()
                if len(actual_params) != expected_arity:
                    self.errors.append(
                        f"Err @ [Line {ctx.start.line}]: Globalna metoda '{method_name}' pozvana sa {len(actual_params)} arg, ocekivano num args: {expected_arity}"
                    )
            #todo nekad, provjeriti outta scope fje gdje kako i kad se pozivaju u klasama (komplkovano)


    def broj_gresaka(self):
            return len(self.errors)


    def exitProg(self, ctx):
        # na kraju check if sve nadklawse postoje
        for cls_name, cls_symbol in self.global_scope.classes.items():
            if cls_symbol.superclass:
                if not self.global_scope.resolve_class(cls_symbol.superclass):
                    self.errors.append(
                        f"Err : Nadklasa '{cls_symbol.superclass}' za klasu '{cls_name}' nije definisana."
                    )

        if self.errors:
            print("Greske:")
            for e in self.errors:
                print("  -", e)
        else:
            print("great success")
