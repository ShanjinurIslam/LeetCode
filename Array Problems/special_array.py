class Solution(object):
    def specialArray(self, nums):
        n = len(nums)
        
        if n == 0:
            return -1
        
        for x in range(1,n+1):
            count = 0
            
            for each in nums:
                if each >= x:
                    count += 1
            
            if count == x:
                return x
        
        return -1
        
        """
        :type nums: List[int]
        :rtype: int
        """
        