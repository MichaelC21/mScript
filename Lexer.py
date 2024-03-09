
_INT = "INTEGER"
_FLOAT = "FLOAT"
_PLUS = "PLUS"
_MINUS = "MINUS"
_MUL = "MUL"
_DIV = "DIV" 
_LBRACKET = "LBRACKET"
_RBRACKET = "RBRACKET"
DIGITS = "1234567890"

class Error:
    def __init__(self, error, details):
        self.error = error
        self.details = details
    
    def __str__(self):
        return self.error + ": " + self.details

class IllegalTokenError(Error):
    def __init__(self, details):
        super().__init__("Illegal character input", details)

class Token():
    def __init__(self, _type, val=None):
        self.type = _type
        self.val = val
    
    def __repr__(self):
        res = self.type
        if self.val:
            res += ": " + str(self.val)
        return res

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
            else:
                char = self.cur_char
                return [], IllegalTokenError(char)
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

def tokenize(text):
    lexer = Lexer(text)
    return lexer.get_tokens()
    
    