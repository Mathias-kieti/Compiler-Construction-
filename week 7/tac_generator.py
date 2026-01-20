class TACGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(self, instruction):
        self.code.append(instruction)

    # Expression: a - b
    def generate_expression(self, left, op, right):
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    # Assignment
    def generate_assignment(self, var, expr):
        self.emit(f"{var} = {expr}")

    # If condition
    def generate_if(self, condition, label):
        self.emit(f"if_false {condition} goto {label}")

    # Labels
    def generate_label(self, label):
        self.emit(f"{label}:")

    # Goto
    def generate_goto(self, label):
        self.emit(f"goto {label}")

    def display(self):
        for line in self.code:
            print(line)
