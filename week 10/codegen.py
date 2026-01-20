class CodeGenerator:
    def __init__(self):
        self.asm = []
        self.label_count = 0

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def generate(self, tac_code):
        for line in tac_code:
            # Handle labels
            if line.endswith(":"):
                self.asm.append(line)
            # Handle goto
            elif line.startswith("goto"):
                label = line.split()[1]
                self.asm.append(f"JMP {label}")
            # Handle conditional jumps
            elif line.startswith("if_false"):
                parts = line.split()
                cond = parts[1]
                label = parts[-1]
                self.asm.append(f"LOAD R1, {cond}")
                self.asm.append(f"JZ {label}")
            elif line.startswith("if_true"):
                parts = line.split()
                cond = parts[1]
                label = parts[-1]
                self.asm.append(f"LOAD R1, {cond}")
                self.asm.append(f"JNZ {label}")
            # Handle assignments
            elif "=" in line:
                left, right = line.split(" = ")
                parts = right.split()

                if len(parts) == 3:
                    a, op, b = parts
                    self.asm.append(f"LOAD R1, {a}")
                    self.asm.append(f"LOAD R2, {b}")

                    if op == "+":
                        self.asm.append("ADD R1, R2")
                    elif op == "-":
                        self.asm.append("SUB R1, R2")
                    elif op == "*":
                        self.asm.append("MUL R1, R2")
                    elif op == "/":
                        self.asm.append("DIV R1, R2")

                    self.asm.append(f"STORE {left}, R1")
                else:
                    self.asm.append(f"LOAD R1, {right}")
                    self.asm.append(f"STORE {left}, R1")

    def display(self):
        for line in self.asm:
            print(line)
