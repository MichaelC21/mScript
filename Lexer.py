from Error import *
from Token import *
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


DIGITS = "1234567890"



class Lexer:
    def __init__(self, text) -> None:
        self.text = text
        self.pos = 0
        self.cur_char = None

    
    def next(self):
        self.cur_char = None
        if  self.pos < len(self.text): 
            self.cur_char = self.text[self.pos]
        self.pos += 1
    
    def get_tokens(self):
        tokens = []
        self.next()
        while self.cur_char != None:
            if self.cur_char == "+":
                tokens.append(Token(_PLUS))
            elif self.cur_char == "-":
                tokens.append(Token(_MINUS))
            elif self.cur_char == "*":
                tokens.append(Token(_MUL))
            elif self.cur_char == "/":
                tokens.append(Token(_DIV))
            elif self.cur_char == "(":
                tokens.append(Token(_LBRACKET))
            elif self.cur_char == ")":
                tokens.append(Token(_RBRACKET))
            elif self.cur_char in DIGITS:
                res = self.getDigit()
                if not res:
                    return []
                tokens.append(res)
                continue
            elif self.cur_char in " \t":
                pass
            elif self.cur_char.isalpha():
                res = self.check_string()
                if not res:
                    return [], IllegalTokenError(self.cur_char)
                tokens.append(res)
            else:
                return [], IllegalTokenError(self.cur_char)
            self.next()
            
            
        return tokens, None
    
    def getDigit(self):
        res = ""
        decimal_count = 0
        while self.cur_char and (self.cur_char in DIGITS or self.cur_char == "."):
            if self.cur_char == ".":
                if decimal_count == 1:
                    return None
                res += self.cur_char
                decimal_count += 1
            else:
                res += self.cur_char  
            self.next()  

        if "." in res:
            return Token(_FLOAT, float(res))
        return Token(_INT, int(res))
    
    def check_string(self):
        res = ""
        while self.cur_char and self.cur_char.isalnum():
            res += self.cur_char
            self.next()
        
        if self.cur_char != None and not self.cur_char.isalnum() and self.cur_char != " ":
            return None    
        
        if res.upper() == "TRUE":
            return Token(_TRUE)
        elif res.upper() == "FALSE":
            return Token(_FALSE)
        return Token(_IDENTIFIER, res)
        
                

def tokenize(text):
    lexer = Lexer(text)
    return lexer.get_tokens()
    
    
