class Solution(object):
    def rob(self, nums):
        N = len(nums)
        
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        
        max_amount = [-1]*N
        
        max_amount[0] = nums[0]
        max_amount[1] = nums[1]
        
        def subproblem(N):
            if N < 0:
                return 0
            
            if max_amount[N] !=-1:
                return max_amount[N]
            else:
                for i in range(0,N-1):
                    max_amount[N] = max(max_amount[N],nums[N] + subproblem(i))
                return max_amount[N]
        
        
        subproblem(N-1)
        subproblem(N-2)
        
        return max(max_amount)