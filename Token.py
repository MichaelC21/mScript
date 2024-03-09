class Token():
    def __init__(self, _type, val=None):
        self.type = _type
        self.val = val
    
    def __repr__(self):
        res = self.type
        if self.val:
            res += ": " + str(self.val)
        return res