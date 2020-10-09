class Solution(object):
    def __init__(self):
        self.ready = [False]*10001
        self.value = [10e10]*10001

    def solve(self, coins, x):
        if x < 0:
            return 10e10
        if (x == 0):
            return 0
        if self.ready[x]:
            return self.value[x]

        best = 10e10
        for c in coins:
            best = min(best, self.solve(coins, x-c) + 1)

        self.ready[x] = True
        self.value[x] = best

        return best

    def coinChange(self, coins, x):
        best = self.solve(coins, x)
        if best == 10e10:
            return -1
        else:
            return best


print(Solution().coinChange([1], 2))
