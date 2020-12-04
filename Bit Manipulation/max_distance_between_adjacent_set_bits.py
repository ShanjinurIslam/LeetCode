class Solution(object):
    def binaryGap(self, n):
        s = bin(n)
        
        indexes = []
        
        for i,each in enumerate(s):
            if each == '1':
                indexes.append(i)
        
        max_val = 0 
        for i in range(0,len(indexes)-1):
            max_val = max( max_val, abs(indexes[i]-indexes[i+1]))
            
        return max_val
            
        """
        :type n: int
        :rtype: int
        """
        