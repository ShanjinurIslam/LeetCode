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

class Solution(object):
    def twoSum(self, nums, target):
        index = dict()
        
        for i,each in enumerate(nums):
            if each in index:
                index[each].append(i)
            else:
                index[each] = [i]
        
        nums = sorted(nums)
        
        i = 0
        j = len(nums) - 1
        
        while(i<j):
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                if nums[i] == nums[j]:
                    return index[nums[i]]
                else:
                    return [index[nums[i]][0],index[nums[j]][0]]
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        