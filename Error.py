'''
    General error class
'''
class Error:
    def __init__(self, error, details=None):
        self.error = error
        self.details = details
    
    def __str__(self):
        if not self.details:
            return self.error
        return self.error + ": " + self.details

'''
    Handles unexpected tokens when doing tokenization
'''
class IllegalTokenError(Error):
    def __init__(self, details):
        super().__init__("Illegal character input", details)
'''
    Handles unexpected syntax in parsing
'''
class IllegalSyntaxError(Error):
    def __init__(self):
        super().__init__("Illegal syntax input")