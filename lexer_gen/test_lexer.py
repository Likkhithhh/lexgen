from output_lexer import Lexer

lexer = Lexer()

while True:
    test_input = input("Enter input (or type 'exit' to quit): ")
    if test_input.lower() == 'exit':
        break
    try:
        tokens = lexer.tokenize(test_input)
        for token in tokens:
            print(token)
    except Exception as e:
        print("Error:", e)
