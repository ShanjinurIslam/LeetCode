class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)
        
        n = len(arr)
        diff = arr[1]-arr[0]
        
        for i in range(n-1):
            if arr[i] + diff != arr[i+1]:
                return False
            
        return True