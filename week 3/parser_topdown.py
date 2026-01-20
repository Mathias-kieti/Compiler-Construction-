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
        stmts = []
        while self.pos < len(self.tokens):
            stmts.append(self.statement())
        return stmts

    def statement(self):
        token = self.tokens[self.pos]
        if token[1] == "if":
            return self.if_statement()
        elif token[1] == "for":
            return self.for_statement()
        elif token[1] == "do":
            return self.do_while_statement()
        elif token[0] == "TYPE":
            return self.declaration()
        else:
            return self.assignment()

    def assignment(self, consume_semicolon=True):
        ident = self.match("IDENTIFIER")
        self.match("OPERATOR")  # =
        expr = self.expression()
        if consume_semicolon:
            self.match("SEPARATOR")
        return {"type": "assignment", "name": ident[1], "value": expr}

    def declaration(self):
        """Parse variable declaration: TYPE IDENTIFIER (= expression)? ;"""
        t = self.match("TYPE")
        ident = self.match("IDENTIFIER")
        value = None
        if self.tokens[self.pos][1] == "=":
            self.match("OPERATOR")
            value = self.expression()
        self.match("SEPARATOR")
        return {"type": "declaration", "data_type": t[1], "name": ident[1], "value": value}

    def if_statement(self):
        self.match("KEYWORD")  # if
        self.match("SEPARATOR")  # (
        condition = self.expression()
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # {
        body = self.statement()
        self.match("SEPARATOR")  # }
        return {"type": "if", "condition": condition, "body": body}

    def for_statement(self):
        self.match("KEYWORD")  # for
        self.match("SEPARATOR")  # (
        init = self.assignment()
        condition = self.expression()
        self.match("SEPARATOR")  # ;
        update = self.assignment(consume_semicolon=False)
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # {
        body = self.statement()
        self.match("SEPARATOR")  # }
        return {"type": "for", "init": init, "condition": condition, "update": update, "body": body}

    def do_while_statement(self):
        self.match("KEYWORD")  # do
        self.match("SEPARATOR")  # {
        body = self.statement()
        self.match("SEPARATOR")  # }
        self.match("KEYWORD")  # while
        self.match("SEPARATOR")  # (
        condition = self.expression()
        self.match("SEPARATOR")  # )
        self.match("SEPARATOR")  # ;
        return {"type": "do_while", "body": body, "condition": condition}

    def expression(self):
        """A very simple expression consumer that gathers tokens until a separator or closing paren."""
        expr_tokens = []
        stop = {')', ';', '}', ']'}
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] not in stop:
            expr_tokens.append(self.tokens[self.pos])
            self.pos += 1
        return ("expr", expr_tokens)
