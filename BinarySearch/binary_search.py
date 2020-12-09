class Solution(object):
    def search(self, nums, target):
        s = 0 
        e = len(nums)-1
        
        while(s<=e):
            mid = (s+e)/2
            
            if nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                return mid
            
        return -1
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        