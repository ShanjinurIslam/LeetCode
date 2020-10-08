# basically you have to perform a dfs to detect a cycle, cycle detection**

class Solution(object):
    def __init__(self):
        self.graph = []
        self.color = []
        self.flag = True

    def dfs_util(self, u):
        self.color[u] = 1

        for adj in self.graph[u]:
            if self.color[adj] == 0:
                self.dfs_util(adj)
            if self.color[adj] == 1:
                self.flag = False

        self.color[u] = 2
        pass

    def dfs(self):
        self.color = [0]*self.N

        for i in range(self.N):
            if self.color[i] == 0:
                self.dfs_util(i)

        return self.flag

    def canFinish(self, numCourses, prerequisites):
        for i in range(numCourses):
            self.graph.append([])

        self.N = numCourses
        self.start = 1

        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            self.graph[u].append(v)

        return self.dfs()


print(Solution().canFinish(4, [[3, 0], [0, 1]]))
