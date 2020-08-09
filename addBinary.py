class Solution(object):
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)

        sum = bin(a+b)

        return str(sum)[2:]
        
        
        