# O(n2) solution

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        rtype = []
        
        for i in range(0,n-1):
            for j in range(1,n):
                if nums[i]+nums[j] == target and i!=j:
                    rtype.append(i)
                    rtype.append(j)
                    
                    return rtype
                
        
class Solution2(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]