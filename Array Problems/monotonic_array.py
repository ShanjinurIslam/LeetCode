class Solution(object):
    def func(self,A):
        flag = True
        
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                flag = False
                break
                
        return flag
    
    
    def isMonotonic(self, A):
        
        flag1 = self.func(A)
        A.reverse()
        flag2 = self.func(A)
                
        return flag1 or flag2
        
        
        """
        :type A: List[int]
        :rtype: bool
        """
        