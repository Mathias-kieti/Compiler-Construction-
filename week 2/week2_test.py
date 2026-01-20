from lexer import tokenize

code = '''
// Sample Zara program for week 2 lexer test
class Demo {
    method void main() {
        int x = 5;
        float y = 3.14;
        string s = "hello";
        array nums = [1, 2, 3];
        stack st;

        // control structures
        if (x >= 5) {
            x = x - 1;
        }

        for (i = 0; i < 10; i = i + 1) {
            st = 0; // push placeholder
        }

        do {
            x = x + 1;
        } while (x != 0);
    }
}
'''

tokens = tokenize(code)
for t in tokens:
    print(t)
