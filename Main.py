import Lexer
import Parser
def main():
    while True:
        line = input("mScript > ")
        if not line:
            break
        res, error = Parser.run(line)
        if error:
            print(str(error))
        else:
            print(res)

main()