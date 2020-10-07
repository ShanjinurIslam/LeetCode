class Solution(object):
    def maxProduct(self, nums):
        N = len(nums)

        max_arr = [0]*N
        min_arr = [0]*N

        max_arr[0] = nums[0]
        min_arr[0] = nums[0]
        result = nums[0]

        for i in range(1, N):
            if nums[i] > 0:
                max_arr[i] = max(nums[i], nums[i]*max_arr[i-1])
                min_arr[i] = min(nums[i], nums[i]*min_arr[i-1])
            else:
                max_arr[i] = max(nums[i], nums[i]*min_arr[i-1])
                min_arr[i] = min(nums[i], nums[i]*max_arr[i-1])

            result = max(max_arr[i], result)

        return result


print(Solution().maxProduct([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
