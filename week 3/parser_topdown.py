class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected_type):
        token = self.tokens[self.pos]
        if token[0] == expected_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Expected {expected_type}, got {token}")

    def parse_program(self):
        while self.pos < len(self.tokens):
            self.statement()

    def statement(self):
        token = self.tokens[self.pos]
        if token[1] == "if":
            self.if_statement()
        elif token[1] == "for":
            self.for_statement()
        elif token[1] == "do":
            self.do_while_statement()
        else:
            self.assignment()

    def assignment(self):
        self.match("IDENTIFIER")
        self.match("OPERATOR")  # =
        self.expression()
        self.match("SEPARATOR")

    def if_statement(self):
        self.match("KEYWORD")  # if
        self.match("SEPARATOR")  # (
        self.expression()
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # {
        self.statement()
        self.match("SEPARATOR")  # }

    def for_statement(self):
        self.match("KEYWORD")  # for
        self.match("SEPARATOR")  # (
        self.assignment()
        self.expression()
        self.match("SEPARATOR")  # ;
        self.assignment()
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # {
        self.statement()
        self.match("SEPARATOR")  # }

    def do_while_statement(self):
        self.match("KEYWORD")  # do
        self.match("SEPARATOR")  # {
        self.statement()
        self.match("SEPARATOR")  # }
        self.match("KEYWORD")  # while
        self.match("SEPARATOR")  # (
        self.expression()
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # ;
