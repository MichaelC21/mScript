from Lexer import *
from Parser import *
class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.cur_node = None
    
    def explore(self, node):
        node_type = type(node).__name__
        if node_type == "DigitNode":
            return self.exploreDigitNode(node)
        elif node_type == "BinaryNode":
            return self.exploreBinaryNode(node, node.left, node.right)
        elif node_type == "UnaryNode":
            return self.exploreUnaryNode(node)
        
    
    def exploreDigitNode(self, node):
        return node

    def exploreBinaryNode(self, node, left, right):
        l = self.explore(left)     
        r = self.explore(right)
        res = self.eval(l,node.op,r)
        return res
   

    def exploreUnaryNode(self, node):
        res = None
        number = self.explore(node.node)
        if node.op.type == "MINUS":
            number = number.token.val * -1
        return DigitNode(Token("INTEGER", number))


    
    def eval(self,left, op, right):
        if op.type == "PLUS":
            value = left.token.val + right.token.val
        elif op.type == "MINUS":
            value = left.token.val - right.token.val
        elif op.type == "MUL":
            value = left.token.val * right.token.val
        elif op.type == "DIV":
            value = left.token.val / right.token.val
        res, err = tokenize(str(value))
        res, err = Parser(res).parse()
        return res

def run(ats):
    interpreter = Interpreter(ats)
    res = interpreter.explore(ats)
    return res.token.val