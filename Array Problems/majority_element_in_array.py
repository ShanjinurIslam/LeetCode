class Solution(object):
    def majorityElement(self, nums):
        hash_map = {}
        for each in nums:
            if each in hash_map:
                hash_map[each] += 1
            else:
                hash_map[each] = 1
        
        arr = []
        
        for each in hash_map.keys():
            arr.append((hash_map[each],each))
            
        return sorted(arr,reverse=True)[0][1]
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        