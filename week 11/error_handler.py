class CompilerError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Error at line {line}, col {column}: {message}" if line else message)


class LexicalError(CompilerError):
    pass


class SyntaxError(CompilerError):
    pass


class SemanticError(CompilerError):
    pass


class ErrorHandler:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def add_error(self, error_type, message, line=None, column=None):
        error = error_type(message, line, column)
        self.errors.append(error)
        return error

    def add_warning(self, message, line=None, column=None):
        self.warnings.append(f"Warning at line {line}, col {column}: {message}" if line else message)

    def has_errors(self):
        return len(self.errors) > 0

    def report(self):
        for error in self.errors:
            print(f"ERROR: {error}")
        for warning in self.warnings:
            print(f"{warning}")
        return len(self.errors)
