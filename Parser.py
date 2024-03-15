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
_KEYWORD = "KEYWORD"
_EQUAL = "EQ"

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
class BinaryNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    #Prints left DigitNode representation the operation and right DigitNode representation
    def __repr__(self):
        return f'({self.left}, {self.op}, {self.right})'

'''
Purpose: Represents a unary operation ex -5
'''
class UnaryNode:
    def __init__(self, op, node):
        self.op = op
        self.node = node
    
    def __repr__(self):
        return f'({self.op}, {self.node})'  

'''
Purpose: Parse a list of given tokens and return an AST
'''
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.stack = []
        self.next()
    
    '''
    Purpose: The starting point of the parse algorithm
    start by calling the lowest precedence (expression)
    Parameters: N/A
    Returns res: ast, err: None (if no error), Error (if error)
    '''
    def parse(self):
        res, err = self.expression()
        # if len(self.stack) > 0:
        #     err = IllegalSyntaxError()
        #self.stack.clear()
        return res, err

    '''
    Purpose: Advance to next token
    Parameters: N/A
    Returns N/A
    '''
    def next(self):
        self.pos += 1 
        if  self.pos < len(self.tokens): 
            self.cur_token = self.tokens[self.pos]
            self.stack.append(self.cur_token)
    
    '''
    Purpose: The highest precedence grammar, responsible for handling digits, 
    unary operations, and brackets
    Parameters: N/A
    Returns res: ast, err: None (if no error), Error (if error)
    '''      
    def factor(self):
        token = self.cur_token
        
        #Unary operation 
        if token.type in (_PLUS, _MINUS):
            self.next()
            factor = self.factor()  #get digit
            if not factor:
                return [], IllegalSyntaxError()
            return UnaryNode(token, factor)   
        elif token.type in (_INT, _FLOAT):     #if digit
            self.next()
            return DigitNode(token)
        elif token.type == _LBRACKET:   #if brackets are involved
            self.next()
            expr, err = self.expression()   #get the expression inside
            if err:
                return [], err
            if self.cur_token.type  == _RBRACKET:  #check for closing
                self.next()
                return expr
            else:
                return [], IllegalSyntaxError()
        else:
            return None
    '''
    Purpose: The second highest precedence grammar, responsible for handling * and / operations
    Parameters: N/A
    Returns res: ast, err: None (if no error), Error (if error)
    '''    
    def term(self):
        left = self.factor()
        if not left:
            return [], IllegalSyntaxError()

        #Consecutive multiply / divide operations in a row
        while self.cur_token.type in (_MUL, _DIV):
            op = self.cur_token
            self.next()
            right = self.factor()
            if not right:
                return [], IllegalSyntaxError()
            self.stack = self.stack[3:]
            left = BinaryNode(left, op, right)
        
        return left, None

    '''
    Purpose: The lowest precedence grammar, responsible for handling + and - operations
    Parameters: N/A
    Returns res: ast, err: None (if no error), Error (if error)
    '''
    def expression(self):
        if self.cur_token.matches(_KEYWORD, "LET"):
            self.next()
            if self.cur_token.type != _IDENTIFIER:
                return [], IllegalSyntaxError()
            var_name = self.cur_token
            self.next()
            if self.cur_token.type != _EQUAL:
                return [], IllegalSyntaxError()
            self.next()
            expr, err = self.expression()
            if err:
                return [], IllegalSyntaxError()
            return expr
        
        left, err = self.term()
        if err:
            return [], err
        
        #Consecutive add / subtract operations in a row
        while self.cur_token.type in (_PLUS, _MINUS):
            op = self.cur_token
            self.next()
            right, err = self.term()
            if err:
                return [], err
            self.stack = self.stack[3:]
            left = BinaryNode(left, op, right)

        
        return left, None

'''
Purpose: Takes a given string tokenizes it then parses it. 
Parameters: text: String
Returns res: ast, err: None (if no error), Error (if error)
'''
def run(text):
    tokens, error = tokenize(text)
    if error:
        return [], error
    
    parser = Parser(tokens)
    ats, error = parser.parse()
    return ats, error
