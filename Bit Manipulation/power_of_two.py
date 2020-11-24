from math import log

class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False        
        a = int(log(n,2))
        return (1<<a) == n