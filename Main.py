import Lexer
import Parser
import Interpreter
import sys

def run_terminal():
    while True:
        line = input("mScript > ")
        if not line:
            break
        res, error = Parser.run(line)
        if error:
            print(str(error))
        else:
            print(Interpreter.run(res))
            
def run_file(f):
    lines = f.read().splitlines() 
    for line in lines:
        res, error = Parser.run(line)
        if error:
            print(str(error))
        else:
            print(Interpreter.run(res))
            
def main():
    if len(sys.argv) > 1 and sys.argv[1][len(sys.argv[1]) - 3:len(sys.argv[1])] == ".ms":
        with open(sys.argv[1], "r") as f:
            run_file(f)
    else:
        run_terminal()
main()