from typing import List


class Solution:
    def __init__(self):
        self.graph = []
        self.all_paths = []

    def printAllPathsUtil(self, s, e, visited, path, path_index):
        visited[s] = True
        path[path_index] = s
        path_index += 1

        if s == e:
            self.all_paths.append(path[:path_index])
        else:
            for each in self.graph[s]:
                if not visited[each]:
                    self.printAllPathsUtil(each, e, visited, path, path_index)

        visited[s] = False
        path_index -= 1

    def printAllPaths(self):
        visited = []
        path = []
        for i in range(self.N):
            visited.append(False)
            path.append(0)

        path_index = 0
        self.printAllPathsUtil(0, self.N-1, visited, path, path_index)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.N = len(graph)
        self.printAllPaths()

        return self.all_paths


solution = Solution()
print(solution.allPathsSourceTarget([[1, 3], [2], [3], []]))
