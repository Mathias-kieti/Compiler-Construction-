class SemanticAnalyzer:
    def __init__(self, symbol_table):
        self.st = symbol_table

    def check_assignment(self, name, value_type, scope):
        symbol = self.st.get_symbol(name, scope)
        if not symbol:
            raise Exception(f"Undeclared variable {name}")
        if symbol.data_type != value_type:
            raise Exception(f"Type mismatch: {symbol.data_type} != {value_type}")
