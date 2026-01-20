import re

class Optimizer:
    def __init__(self, tac_code):
        self.code = tac_code

    def constant_folding(self):
        optimized = []
        for line in self.code:
            match = re.match(r"(t\d+) = (\d+) ([+\-*/]) (\d+)", line)
            if match:
                temp, a, op, b = match.groups()
                result = eval(f"{a}{op}{b}")
                optimized.append(f"{temp} = {result}")
            else:
                optimized.append(line)
        self.code = optimized

    def dead_code_elimination(self):
        used = set()
        for line in self.code:
            parts = line.split()
            for p in parts:
                if p.startswith("t"):
                    used.add(p)

        self.code = [
            line for line in self.code
            if not (line.startswith("t") and line.split(" = ")[0] not in used)
        ]

    def display(self):
        for line in self.code:
            print(line)
