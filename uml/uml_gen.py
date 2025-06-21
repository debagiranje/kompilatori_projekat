import os
from antlr4 import *
import sys
sys.path.append(r"/home/ng/Documents/kompilatori_projekat/sintaksni_analizator")
sys.path.append(r"/home/ng/Documents/kompilatori_projekat/leksicki_analizator")
from RubyLekser import RubyLekser
from RubyParser import RubyParser
from RubyParserListener import RubyParserListener


class AttributeInfo:
    def __init__(self, name, visibility="public", accessor=None):
        self.name = name
        self.visibility = visibility
        self.accessor = accessor

class MethodInfo:
    def __init__(self, name, visibility="public", parameters=None, return_type=None):
        self.name = name
        self.visibility = visibility
        self.parameters = parameters if parameters else []
        self.return_type = return_type

class ClassInfo:
    def __init__(self, name, superclass=None):
        self.name = name
        self.superclass = superclass
        self.methods = {"public": [], "protected": [], "private": []}
        self.attributes = {"public": [], "protected": [], "private": []}

    def add_attribute(self, attr: AttributeInfo):
        if attr.visibility not in self.attributes:
            self.attributes[attr.visibility] = []
        self.attributes[attr.visibility].append(attr)

    def add_method(self, method: MethodInfo):
        if method.visibility not in self.methods:
            self.methods[method.visibility] = []
        self.methods[method.visibility].append(method)

class UMLListener(RubyParserListener):
    def __init__(self):
        super().__init__()
        self.classes = []
        self.current_class = None
        self.current_visibility = "public"

    def enterClass_definition(self, ctx):
        name = ctx.klasa.getText()
        superclass = ctx.nadklasa.getText() if ctx.nadklasa else None
        self.current_class = ClassInfo(name, superclass)
        self.classes.append(self.current_class)
        self.current_visibility = "public"

    def exitClass_definition(self, ctx):
        self.current_class = None
        self.current_visibility = "public"

    def enterMethod_definition(self, ctx):
        vis = ctx.m.getText().strip() if ctx.m else "public"
        self.current_visibility = vis

        header = ctx.method_definition_header()
        method_name_ctx = header.method_name()
        if method_name_ctx is None:
            return

        if method_name_ctx.id_method():
            name = method_name_ctx.id_method().getText()
        elif method_name_ctx.id_():
            name = method_name_ctx.id_().getText()
        else:
            name = "anon"

        param_list_ctx = header.method_definition_params()
        param_names = []

        if param_list_ctx and param_list_ctx.method_definition_params_list():
            
            def extract_param_ids(pctx):
                if pctx.method_definition_params_list():
                    extract_param_ids(pctx.method_definition_params_list())
                if pctx.method_definition_param_id():
                    param_names.append(pctx.method_definition_param_id().getText())

            
            extract_param_ids(param_list_ctx.method_definition_params_list())

        if self.current_class:
            method_info = MethodInfo(name, visibility=vis, parameters=param_names)
            self.current_class.add_method(method_info)

    def enterInstance_variable_assignment(self, ctx):
        var_name = ctx.instance_var().getText()
        vis = "private"  
        if self.current_class:
            attr_info = AttributeInfo(var_name, visibility=vis)
            self.current_class.add_attribute(attr_info)

    def enterAttribute_definition(self, ctx):
        accessor_type = ctx.attr_type().getText()

        attr_names = [idctx.getText() for idctx in ctx.id_()]

        # add svaki atribut u trenutnu klasu
        for attr_name in attr_names:
            if self.current_class:
                attr_info = AttributeInfo(attr_name, visibility="private", accessor=accessor_type)
                self.current_class.add_attribute(attr_info)

    
    def enterVisibility_modifier(self, ctx):
        vis = ctx.getText().strip()
        self.current_visibility = vis

def generate_plantuml(classes):
    visibility_map = {"public": "+", "protected": "#", "private": "-"}
    lines = ["@startuml"]

    for uml_class in classes:
        lines.append(f"class {uml_class.name} {{")

        # Atributi klase
        for vis, attrs in uml_class.attributes.items():
            symbol = visibility_map.get(vis, "+")
            for attr in attrs:
                lines.append(f"  {symbol} {attr.name}")

        # Metode
        for vis, methods in uml_class.methods.items():
            symbol = visibility_map.get(vis, "+")
            for method in methods:
                params = ", ".join(method.parameters)
                lines.append(f"  {symbol} {method.name}({params})")

        # getteri i setteri za attrs definisani preko attr_accessor / reader / writer
        # note getteri i setteri su public uvijek, a attrs su uvijek private
        for vis, attrs in uml_class.attributes.items():
            symbol = "+"
            for attr in attrs:
                if attr.accessor in ("attr_accessor", "attr_reader"):
                    lines.append(f"  {symbol} {attr.name}()")
                if attr.accessor in ("attr_accessor", "attr_writer"):
                    lines.append(f"  {symbol} {attr.name}=(val)")

        lines.append("}")

        # nasljedjivanje
        if uml_class.superclass:
            lines.append(f"{uml_class.superclass} <|-- {uml_class.name}")

    lines.append("@enduml")
    return "\n".join(lines)


def codegen(fajl):
    input_stream = FileStream(f"/home/ng/Documents/kompilatori_projekat/primjeri/{fajl}.rb", encoding='utf-8')
    lexer = RubyLekser(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = RubyParser(tokens)
    tree = parser.prog()

    walker = ParseTreeWalker()
    uml_listener = UMLListener()
    walker.walk(uml_listener, tree)

    uml_code = generate_plantuml(uml_listener.classes)
    print(uml_code)
    return uml_code