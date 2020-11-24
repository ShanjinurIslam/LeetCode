class Solution(object):
    def hammingWeight(self, n):
        i = 0
        sum = 0
        
        while i<32:
            if (n & 1) == 1:
                sum += 1
                
            n = n >> 1 
            i += 1
            
        return sum
        """
        :type n: int
        :rtype: int
        """
        