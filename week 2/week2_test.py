from lexer import tokenize

code = '''
int x = 5;
if (x > 3) {
    x = x - 1;
}
'''

tokens = tokenize(code)
for t in tokens:
    print(t)
