# O(n) Solution

class Solution(object):
    def productExceptSelf(self, nums):
        N = len(nums)

        result = [0]*N

        result[0] = 1

        for i in range(1, N):
            result[i] = result[i-1] * nums[i-1]

        right = 1
        for i in range(N-1, -1, -1):
            result[i] = result[i] * right
            right = right*nums[i]

        return result
