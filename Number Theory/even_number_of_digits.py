from math import log10,floor

class Solution(object):
    def findNumbers(self, nums):
        count = 0 
        
        for each in nums:
            if ((int(floor(log10(each))) + 1) % 2) == 0 :
                count += 1
                
        return count 
                
        
        """
        :type nums: List[int]
        :rtype: int
        """
        