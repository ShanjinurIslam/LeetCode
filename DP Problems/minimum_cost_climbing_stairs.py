# DP Solution

# Approach

'''
Start from last and second last stair and recursively call previous stairs.
Save minimum cost to array in order to minimize function calls 
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        calculated = [-1]*n
        min_cost = [2e10]*n
        
        min_cost[0] = cost[0]
        calculated[0] = 1
        
        min_cost[1] = cost[1]
        calculated[1] = 1
        
        def subproblem(N):
            if calculated[N] != -1:
                return min_cost[N]
            else:
                min_cost[N] = min(cost[N]+subproblem(N-1),cost[N]+subproblem(N-2))
                calculated[N] = 1
                return min_cost[N]
            
        return min(subproblem(n-1),subproblem(n-2))
        
        """
        :type cost: List[int]
        :rtype: int
        """
        