class Solution(object):
    def moveZeroes(self, nums):
        numZeros = 0
        n = len(nums)
        
        arr = []
        
        for i in range(n):
            if nums[i] == 0:
                numZeros += 1
            else:
                arr.append(nums[i])
                
        for i in range(numZeros):
            arr.append(0)
            
        for i in range(n):
            nums[i] = arr[i]
        
        
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        