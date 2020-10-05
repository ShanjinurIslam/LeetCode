class Solution(object):
    def canReach(self, arr, start):
        N = len(arr)

        queue = []
        visited = [False]*N

        queue.append(start)
        queue_len = 1
        zero_visited = False

        while(queue_len > 0):
            s = queue[0]
            queue.pop(0)
            queue_len -= 1

            if not visited[s]:
                visited[s] = True
                if arr[s] == 0:
                    zero_visited = True
                    break

            else:
                continue

            left_index = s - arr[s]
            right_index = s + arr[s]

            if left_index >= 0:
                queue.append(left_index)
                queue_len += 1

            if right_index < N:
                queue.append(right_index)
                queue_len += 1

        if zero_visited:
            return True
        else:
            return False
