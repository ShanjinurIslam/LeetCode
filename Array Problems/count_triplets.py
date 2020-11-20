class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        
        count = 0 
        n = len(arr)
        for i in range(n-2):
            for j in range(i,n-1):
                for k in range(j,n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c and i < j and j < k:
                        count += 1
                    
                    
        
        return count
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        