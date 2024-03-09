import Lexer
def main():
    while True:
        line = input("mScript > ")
        if not line:
            break
        res, error = Lexer.tokenize(line)
        if error:
            print(str(error))
        else:
            print(res)

main()