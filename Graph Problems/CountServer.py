class Solution(object):
    def __init__(self):
        self.grid = []

    def dfs(self):
        self.visited = []
        for i in range(self.m):
            self.visited.append([])
            for j in range(self.n):
                self.visited[i] = [False]*self.n

        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    visits = self.dfs_util(i, j)
                    if visits > 1:
                        count += visits

        return count

    def dfs_util(self, i, j):
        if not self.grid[i][j] == 1:
            return 0
        self.visited[i][j] = True
        total = 1

        for k in range(0, self.n):
            if k != j and not self.visited[i][k]:
                total = total + self.dfs_util(i, k)

        for k in range(0, self.m):
            if k != i and not self.visited[k][j]:
                total = total + self.dfs_util(k, j)

        return total

    def countServers(self, grid):
        self.grid = grid

        self.m = len(grid)
        self.n = len(grid[0])

        return self.dfs()


solution = Solution()
print(solution.countServers(
    [[0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 0, 1, 1], [0, 0, 1, 1, 0]]))
