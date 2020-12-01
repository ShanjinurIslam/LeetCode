class Solution(object):
    def singleNumber(self, nums):
        hash_map = {}
        
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
            
        
        for key in hash_map.keys():
            if hash_map[key] == 1:
                return key
        
        """
        :type nums: List[int]
        :rtype: int
        """
        