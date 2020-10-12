class Solution(object):
    def dfs_util(self, i, j):
        if self.visited[i][j] == True:
            return
        else:
            self.visited[i][j] = True
            if i+1 < self.n and self.visited[i+1][j] == False and self.grid[i+1][j] == "1":
                self.dfs_util(i+1, j)

            if j+1 < self.m and self.visited[i][j+1] == False and self.grid[i][j+1] == "1":
                self.dfs_util(i, j+1)

            if i-1 >= 0 and self.visited[i-1][j] == False and self.grid[i-1][j] == "1":
                self.dfs_util(i-1, j)

            if j-1 >= 0 and self.visited[i][j-1] == False and self.grid[i][j-1] == "1":
                self.dfs_util(i, j-1)

    def numIslands(self, grid):
        self.grid = grid
        self.n = len(grid)
        if self.n > 0:
            self.m = len(grid[0])

        self.visited = []

        for i in range(self.n):
            self.visited.append([])
            for j in range(self.m):
                self.visited[i] = [False]*self.m

        islands = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.visited[i][j] == False and self.grid[i][j] == "1":
                    self.dfs_util(i, j)
                    islands += 1

        return islands


print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
