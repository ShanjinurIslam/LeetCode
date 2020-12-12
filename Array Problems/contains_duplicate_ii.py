class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        found = dict()
        
        for i,each in enumerate(nums):
            if each in found:
                found[each].append(i)
            else:
                found[each] = [i]
                
        for each in found.items():
            n = len(each[1])
            if n>1:
                for i in range(n-1):
                    if abs(each[1][i]-each[1][i+1]) <= k:
                        return True
        return False
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        