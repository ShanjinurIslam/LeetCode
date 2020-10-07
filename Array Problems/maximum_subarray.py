# Kadane's Algorithm
class Solution(object):
    def maxSubArray(self, nums):
        best = nums[0]
        total = nums[0]

        N = len(nums)

        for i in range(1, N):
            total = max(nums[i], total + nums[i])
            best = max(total, best)

        return best
