def safe_parse(parser):
    try:
        parser.parse_program()
    except SyntaxError as e:
        print("Syntax Error:", e)
        print("Skipping to next statement...")
