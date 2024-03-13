from Lexer import *
from Parser import *
'''
    Interpreter Class
'''
class Interpreter:
    def __init__(self, ast):
        self.ast = ast  
        self.cur_node = None
    
    '''
        Purpose:    Explores various types of nodes
        Parameters: node, NodeType
        Returns: The final evaluation of the node
    '''
    def explore(self, node):
        node_type = type(node).__name__
        if node_type == "DigitNode":
            return self.exploreDigitNode(node)
        elif node_type == "BinaryNode":
            return self.exploreBinaryNode(node, node.left, node.right)
        elif node_type == "UnaryNode":
            return self.exploreUnaryNode(node)
        
    '''
        Purpose: returns node of the digit
        Parameters: node Node
        Returns: DigitNode
    '''
    def exploreDigitNode(self, node):
        return node

    '''
        Purpose: explores the left and right nodes and calls eval on both
        Parameters: node Node, left Node, right Node
        Returns: Node
    '''
    def exploreBinaryNode(self, node, left, right):
        l = self.explore(left)     
        r = self.explore(right)
        res = self.eval(l,node.op,r)
        return res
   
    '''
        Purpose: Checks the type of the unary node
        Parameters: node, Node
        Returns: DigitNode
    '''
    def exploreUnaryNode(self, node):
        res = None
        number = self.explore(node.node)
        if node.op.type == "MINUS":
            number = number.token.val * -1
        return DigitNode(Token("INTEGER", number))


    '''
        Purpose: Evals the left, right, and op
        Parameters: left Node, op Node, right Node
        Returns: Node
    '''
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

'''
    Purpose: Entry point for interpreter
    Parameters: ats Node
    Returns: val Int
'''
def run(ats):
    interpreter = Interpreter(ats)
    res = interpreter.explore(ats)
    return res.token.val