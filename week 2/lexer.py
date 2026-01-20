import re

TOKEN_SPEC = [
    ('KEYWORD', r'\b(if|else|for|do|while|class|method)\b'),
    ('TYPE', r'\b(int|float|string|array|stack)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER', r'\b\d+(\.\d+)?\b'),
    ('STRING', r'"[^"]*"'),
    ('OPERATOR', r'==|=|\*|/|-|>'),
    ('SEPARATOR', r'[();{},]'),
    ('WHITESPACE', r'\s+'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':
            tokens.append((kind, value))
    return tokens
