class Solution(object):
    def canVisitAllRooms(self, rooms):
        self.graph = rooms
        N = len(self.graph)

        queue = []
        visited = [False]*len(self.graph)

        queue.append(0)
        queue_len = 1
        total_visited = 0

        while(queue_len > 0):
            s = queue[0]
            queue.pop(0)
            queue_len -= 1

            if not visited[s]:
                visited[s] = True
                total_visited += 1
            else:
                continue

            for adj in self.graph[s]:
                if not visited[adj]:
                    queue.append(adj)
                    queue_len += 1

        if total_visited == N:
            return True
        else:
            return False


solution = Solution()
print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
