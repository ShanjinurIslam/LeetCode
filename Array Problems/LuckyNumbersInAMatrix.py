class Solution(object):
    def col(self,matrix,i):
        return [row[i] for row in matrix]
    
    def luckyNumbers (self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        
        row_mins = set()
        for i in range(n):
            row_mins.add(min(matrix[i]))
            
        col_maxs = set()
        for i in range(m):
            col_maxs.add(max(self.col(matrix,i)))
            
        return list(row_mins.intersection(col_maxs))
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        