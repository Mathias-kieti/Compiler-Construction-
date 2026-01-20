class ShiftReduceParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def parse(self):
        for token in self.tokens:
            if token[0] == "NUMBER" or token[0] == "IDENTIFIER":
                self.stack.append(token)
            elif token[1] in self.precedence:
                while len(self.stack) >= 3:
                    a, op, b = self.stack[-3:]
                    if self.can_reduce(op, token):
                        self.stack = self.stack[:-3]
                        self.stack.append(("EXPR", f"{a[1]} {op[1]} {b[1]}"))
                    else:
                        break
                self.stack.append(token)
            elif token[1] == ";":
                self.reduce_all()
        return self.stack

    def can_reduce(self, op1, op2):
        return self.precedence.get(op1[1], 0) >= self.precedence.get(op2[1], 0)

    def reduce_all(self):
        while len(self.stack) >= 3:
            a, op, b = self.stack[-3:]
            self.stack = self.stack[:-3]
            self.stack.append(("EXPR", f"{a[1]} {op[1]} {b[1]}"))
