class Solution(object):
    def containsDuplicate(self, nums):
        N = len(nums)

        if N == 0:
            return False

        nums = sorted(nums)
        previous = nums[0]

        for i in range(1, N):
            if previous == nums[i]:
                return True
            else:
                previous = nums[i]

        return False


print(Solution().containsDuplicate([1, 2, 3]))
