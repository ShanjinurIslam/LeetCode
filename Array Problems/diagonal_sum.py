class Solution(object):
    def diagonalSum(self, mat):
        
        n = len(mat[0])
        sum = 0
        
        for i in range(n):
            if i == n-1-i:
                sum += mat[i][i]
            else:
                sum += mat[i][i]
                sum += mat[n-1-i][i]
            
        return sum
        
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        