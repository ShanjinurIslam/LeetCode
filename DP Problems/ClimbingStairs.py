class Solution(object):
    def __init__(self):
        self.steps = [-1]*50

    def climbStairs(self, n):
        if self.steps[n] != -1:
            return self.steps[n]

        if n < 1:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        else:
            self.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.steps[n]


print(Solution().climbStairs(4))
