class Solution(object):
    def findRelativeRanks(self, nums):
        index_map = {}
        ranks = ["-1"]*len(nums)
        
        for i,each in enumerate(nums):
            index_map[each] = i
        
        nums = sorted(nums,reverse=True)
        
        curr = 1
        
        for each in nums:
            if curr == 1:
                ranks[index_map[each]] = "Gold Medal"
            elif curr == 2:
                ranks[index_map[each]] = "Silver Medal"
            elif curr == 3:
                ranks[index_map[each]] = "Bronze Medal"
            else:
                ranks[index_map[each]] = str(curr)
                
            curr += 1
            
        return ranks
        
        
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        