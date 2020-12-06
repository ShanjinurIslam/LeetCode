class Solution(object):
    def maxScore(self, s):
        max_val = -1
        
        for i in range(1,len(s)):
            zeros = s[:i].count('0')
            ones = s[i:].count('1')
            
            max_val = max(max_val,zeros+ones)
            
        return max_val
        
        
        """
        :type s: str
        :rtype: int
        """
        