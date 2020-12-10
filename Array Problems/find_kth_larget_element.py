class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums,reverse=True)[k-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        