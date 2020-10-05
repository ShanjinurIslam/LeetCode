from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = []
        self.N = n
        self.vertices = range(self.N)

        for i in self.vertices:
            self.graph.append([])
            self.graph[i] = 0

        for each in edges:
            self.graph[each[1]] += 1

        minimum = []

        for i in self.vertices:
            if self.graph[i] == 0:
                minimum.append(i)

        return sorted(minimum)


print(Solution().findSmallestSetOfVertices(
    4,
    [[1, 3], [2, 0], [2, 3], [1, 0], [4, 1], [0, 3]]))
