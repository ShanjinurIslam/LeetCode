class Solution(object):
    def recur(self,N,arr):
        if N == 0:
            arr[0] = 0
            return 0
        if N == 1:
            arr[1] = 1
            return 1
        if N == 2:
            arr[2] = 1
            return 1
        
        else:
            if arr[N] != 0:
                return arr[N]
            else:
                arr[N] = self.recur(N-1,arr) + self.recur(N-2,arr) + self.recur(N-3,arr)
                return arr[N]
            
    def tribonacci(self, N):
        arr = [0]*(N+1)
        
        return self.recur(N,arr)
        """
        :type n: int
        :rtype: int
        """
        