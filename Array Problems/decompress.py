class Solution(object):
    def decompressRLElist(self, nums):
        decomposed = []
        
        i = 0
        size = len(nums)
        
        while(i<size):
            freq = nums[i]
            val = nums[i+1]
            
            out = [int(val)]*freq
            decomposed.extend(out)
            
            i += 2
            
        return decomposed
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        