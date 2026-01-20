class IntermediateCode:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(self, instruction):
        self.code.append(instruction)

    def translate_expression(self, expr):
        """Translate simple expression to TAC"""
        if len(expr) == 3 and expr[1] in ['+', '-', '*', '/']:
            temp = self.new_temp()
            self.emit(f"{temp} = {expr[0]} {expr[1]} {expr[2]}")
            return temp
        return expr[0] if isinstance(expr, (list, tuple)) else expr

    def display(self):
        for line in self.code:
            print(line)
