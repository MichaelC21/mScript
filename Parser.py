from Lexer import *
from Error import *
_INT = "INTEGER"
_FLOAT = "FLOAT"
_PLUS = "PLUS"
_MINUS = "MINUS"
_MUL = "MUL"
_DIV = "DIV" 
_LBRACKET = "LBRACKET"
_RBRACKET = "RBRACKET"
_TRUE = "TRUE"
_FALSE = "FALSE"
_IDENTIFIER = "IDENTIFIER" 

'''
Purpose: Represents a digit (int or float)
'''
class DigitNode:
    def __init__(self, token):
        self.token = token
    
    #Prints token representation
    def __repr__(self):
        return f'{self.token}'

'''
Purpose: Represents a binary operation (left digit) + (an operation) + (right digit)
'''
class OperationNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    #Prints left DigitNode representation the operation and right DigitNode representation
    def __repr__(self):
        return f'({self.left}, {self.op}, {self.right})'
    

'''
Purpose: Represents a binary operation (left digit) + (an operation) + (right digit)
'''
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.stack = []
        self.next()
    
    def parse(self):
        res, err = self.expression()
        if len(self.stack) > 0:
            err = IllegalSyntaxError()
        self.stack.clear()
        return res, err

    def next(self):
        self.pos += 1 
        if  self.pos < len(self.tokens): 
            self.cur_token = self.tokens[self.pos]
            self.stack.append(self.cur_token)
    def factor(self):
        token = self.cur_token
        if token.type in (_INT, _FLOAT):
            self.next()
            return DigitNode(token.val)
        else:
            return None

    def term(self):
        left = self.factor()
        if not left:
            return [], IllegalSyntaxError()

        while self.cur_token.type in (_MUL, _DIV):
            op = self.cur_token
            self.next()
            right = self.factor()
            if not right:
                return [], IllegalSyntaxError()
            self.stack = self.stack[3:]
            left = OperationNode(left, op, right)
        
        return left, None

    def expression(self):
        left, err = self.term()
        if err:
            return [], err

        while self.cur_token.type in (_PLUS, _MINUS):
            op = self.cur_token
            self.next()
            right, err = self.term()
            if err:
                return [], err
            self.stack = self.stack[3:]
            left = OperationNode(left, op, right)

        
        return left, None

def run(text):
    tokens, error = tokenize(text)
    if error:
        return [], error
    
    parser = Parser(tokens)
    ats, error = parser.parse()
    return ats, error
