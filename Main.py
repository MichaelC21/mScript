import Lexer
import Parser
import Interpreter
def main():
    while True:
        line = input("mScript > ")
        if not line:
            break
        res, error = Parser.run(line)
        if error:
            print(str(error))
        else:
            print(Interpreter.run(res))

main()