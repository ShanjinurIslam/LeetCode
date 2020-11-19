class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for i in range(0,n):
            arr.append(nums[i])
            arr.append(nums[n+i])
            
        return arr