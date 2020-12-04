class Solution(object):
    def col(self,A,n,col):
        arr = []
        
        for i in range(n):
            arr.append(A[i][col])
            
        return arr
    
    def transpose(self, A):
        n = len(A)
        m = len(A[0])
        
        if n == m:
            for i in range(0,n):
                for j in range(i,m):
                    if j != i:
                        temp = A[i][j]
                        A[i][j] = A[j][i]
                        A[j][i] = temp

            return A
        
        else:
            final = []
            for i in range(m):
                final.append(self.col(A,n,i))
                
            return final
        
        
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        