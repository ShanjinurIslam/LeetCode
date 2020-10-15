# have to worry about address not value

class Solution(object):
    def hasCycle(self, head):
        visited = {}
        cur = 0
        pos = -1

        while(head != None):
            if head in visited:  # saves object in hashmap
                return True
            else:
                visited[head] = 1

            head = head.next
            cur += 1

        return False
