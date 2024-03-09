class Error:
    def __init__(self, error, details=None):
        self.error = error
        self.details = details
    
    def __str__(self):
        if not self.details:
            return self.error
        return self.error + ": " + self.details

class IllegalTokenError(Error):
    def __init__(self, details):
        super().__init__("Illegal character input", details)

class IllegalSyntaxError(Error):
    def __init__(self):
        super().__init__("Illegal syntax input")