class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        n = len(arr)
        
        for i in range(1,n+1):
            if i%2 == 0:
                continue
            else:
                for k in range(0,n-i+1):
                    total += sum(arr[k:k+i])
        
        return total
        
        """
        :type arr: List[int]
        :rtype: int
        """
        