class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        
        n = len(nums)
        sum = 0 
        
        for i in range(0,n-1,2):
            sum += nums[i]
            
        return sum
        
        """
        :type nums: List[int]
        :rtype: int
        """
        