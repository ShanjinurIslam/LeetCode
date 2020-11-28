class Solution(object):
    def findDuplicate(self, nums):
        nums = sorted(nums)
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
            
        return -1
        
        """
        :type nums: List[int]
        :rtype: int
        """
        