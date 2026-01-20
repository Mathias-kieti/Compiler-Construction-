# Simple test for week 4 bottom-up parser (shift-reduce style)
from importlib import util

spec = util.spec_from_file_location('parser_bottomup', 'week 4/parser_bottomup.py')
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

# Tokens: simple expression: 2 + 3 * 4 ;
# Format: (TOKEN_TYPE, TOKEN_VALUE)
tokens = [
    ('NUMBER', '2'),
    ('OPERATOR', '+'),
    ('NUMBER', '3'),
    ('OPERATOR', '*'),
    ('NUMBER', '4'),
    ('SEPARATOR', ';')
]

parser = mod.ShiftReduceParser(tokens)
result = parser.parse()
print('Shift-reduce parse result:')
print(result)
