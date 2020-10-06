class Solution(object):
    def __init__(self):
        self.graph = []
        self.visited = []
        self.flag = True

    def dfs_util(self, u):
        if self.visited[u]:
            return
        else:
            self.visited[u] = True
            for j in self.graph[u]:
                if not self.visited[j]:
                    if self.color[u] == 1:
                        self.color[j] = 2
                    else:
                        self.color[j] = 1
                    self.dfs_util(j)

                else:
                    if self.color[u] == self.color[j]:
                        self.flag = False

    def dfs(self):
        self.visited = [False]*self.N
        self.color = [0]*self.N
        self.flag = True

        for i in range(self.N):
            if not self.visited[i]:
                self.color[i] = 1
                self.dfs_util(i)

        return self.flag

    def isBipartite(self, graph):
        self.graph = graph
        self.N = len(graph)

        return self.dfs()


solution = Solution()
print(solution.isBipartite([[1], [0], [4], [4], [2, 3]]))
