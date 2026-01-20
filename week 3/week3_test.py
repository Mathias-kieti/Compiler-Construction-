import importlib.util

# Load lexer from 'week 2/lexer.py'
lexer_spec = importlib.util.spec_from_file_location("lexer", "week 2/lexer.py")
lexer = importlib.util.module_from_spec(lexer_spec)
lexer_spec.loader.exec_module(lexer)

# Load top-down parser from 'week 3/parser_topdown.py'
parser_spec = importlib.util.spec_from_file_location("parser_topdown", "week 3/parser_topdown.py")
parser = importlib.util.module_from_spec(parser_spec)
parser_spec.loader.exec_module(parser)

code = '''
int x = 5;
if (x > 3) {
    x = x - 1;
}
for (i = 0; i < 3; i = i + 1) {
    x = x + i;
}
'''

print("Source:\n", code)

tokens = lexer.tokenize(code)
print("\nTokens:")
for t in tokens:
    print(t)

print("\nParsing...")
p = parser.Parser(tokens)
ast = p.parse_program()
print("\nAST:\n", ast)
