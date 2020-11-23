class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        max = -1
        final = [0]*n
        final[-1] = max
        
        for i in range(n-2,-1,-1):
            if arr[i+1] > max:
                max = arr[i+1]
                final[i] = max
            else:
                final[i] = max
            
        return final
        
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        