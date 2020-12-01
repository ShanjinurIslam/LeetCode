# Approach

'''
c 3 2 2 1 1 1 0
b 3 2 2 1 1 1 1
a 3 2 2 2 2 2 2
  3 3 3 3 3 3 3 
    a h b g d c

As matrix achieved 0 then isASubsequence

'''

class Solution(object):
    def isSubsequence(self, s, t):
        N = len(s)
        M = len(t)
        
        matrix = []
        
        for i in range(N+1):
            matrix.append([])
            for j in range(M+1):
                if j == 0 or i == 0:
                    matrix[i].append(N)
                else:
                    matrix[i].append(0)
        
        for i in range(1,N+1):
            for j in range(1,M+1):
                if s[i-1] == t[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] - 1
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1])
        
        return True if min([min(each) for each in matrix]) == 0 else False
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        