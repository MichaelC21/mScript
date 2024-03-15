class Token():
    def __init__(self, _type, val=None):
        self.type = _type
        self.val = val
    
    def matches(self, key, val):
        if self.type == key and self.val == val:
            return True
        return False
    
    def __repr__(self):
        res = self.type
        if self.val:
            res += ": " + str(self.val)
        return res