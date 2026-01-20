class Symbol:
    def __init__(self, name, data_type, scope, value=None):
        self.name = name
        self.data_type = data_type
        self.scope = scope
        self.value = value

    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.data_type}, scope={self.scope}, value={self.value})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, data_type, scope, value=None):
        key = (name, scope)
        if key in self.symbols:
            raise Exception(f"Symbol {name} already declared in scope {scope}")
        self.symbols[key] = Symbol(name, data_type, scope, value)

    def update_symbol(self, name, scope, value):
        key = (name, scope)
        if key not in self.symbols:
            raise Exception(f"Symbol {name} not found")
        self.symbols[key].value = value

    def get_symbol(self, name, scope):
        return self.symbols.get((name, scope), None)

    def display(self):
        for sym in self.symbols.values():
            print(sym)
