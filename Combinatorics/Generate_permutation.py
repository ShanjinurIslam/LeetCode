class Solution(object):
    def search(self,permutation,chosen,n,arr):
        if(len(permutation)==n):
            arr.append(permutation[:])
            return
        else:
            for i in range(n):
                if chosen[i]:
                    continue
                chosen[i] = True
                permutation.append(self.nums[i])
                self.search(permutation,chosen,n,arr)
                chosen[i] = False
                permutation.pop()
    
    def permute(self, nums):
        self.nums = nums
        n = len(nums)
        chosen = [False]*n
        permutation = []
        
        arr = []
        self.search(permutation,chosen,n,arr)
        
        return arr
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        