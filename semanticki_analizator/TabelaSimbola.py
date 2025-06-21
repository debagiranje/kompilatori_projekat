class Scope:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.classes = {}  

    def define_class(self, cls):
        self.classes[cls.name] = cls

    def resolve_class(self, name):
        #Trazi klasu rekurzivno kroz roditeljske scope-ove
        if name in self.classes:
            return self.classes[name]
        elif self.parent:
            return self.parent.resolve_class(name)
        else:
            return None

class ClassSymbol:
    def __init__(self, name, superclass=None):
        self.name = name
        self.superclass = superclass
        self.methods = {}    
        self.attributes = set()  

    def define_method(self, name, method_symbol):
        self.methods[name] = method_symbol

    def resolve_method(self, name):
        return self.methods.get(name, None)


class MethodSymbol:
    def __init__(self, name, parameters=None):
        self.name = name
        self.parameters = parameters or [] 

    def arity(self):
        return len(self.parameters)
