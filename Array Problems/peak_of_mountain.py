class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        
        ie = 0
        
        for i in range(0,n-1):
            if arr[i] < arr[i+1]:
                ie = i+1
            else:
                break
                
        
        return ie