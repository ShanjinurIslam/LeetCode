class Solution(object):    
    def balancedStringSplit(self, s):
        count = 0
        res = 0
        
        for each in s:
            if each == 'L':
                res += 1
            else:
                res -= 1
            
            if res == 0:
                count += 1
        
        return count
        
        """
        :type s: str
        :rtype: int
        """
        