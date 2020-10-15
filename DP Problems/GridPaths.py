from math import factorial

class Solution(object):
    def uniquePaths(self, m, n):
        m -= 1 
        n -= 1
        
        return factorial(m+n)/(factorial(m)*factorial(n))
        
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        