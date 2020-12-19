class Solution(object):
    def rotateString(self, A, B):
        if len(A)!=len(B):
            return False
        
        if A==B:
            return True
        
        for i in range(len(A)-1):
            custom = A[i+1:] + A[:i+1]
            if custom == B:
                return True
        
        return False
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        