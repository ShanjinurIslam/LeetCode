# bfs technique
# djkastra

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        # graph problem
        
        dist = []
        visited = []
        
        for i in range(R):
            dist.append([])
            visited.append([])
            
            for j in range(C):
                dist[i].append(10e10)
                visited[i].append(False)
        
        queue = []
    
        queue.append((0,(r0,c0)))
        dist[r0][c0] = 0
        
        arr = []
        
        while(len(queue)>0):
            dist_val,(r,c) = queue.pop(0)
            arr.append([r,c])
            
            if visited[r][c]:
                continue
            else:
                visited[r][c] = True
                
                for i in range(r-1,r+2,1):
                    for j in range(c-1,c+2,1):
                        if i>=0 and i<R and j>=0 and j<C and not visited[i][j]:
                            val = dist[r][c] + (abs(i-r)+abs(j-c))
                            if dist[i][j] > val:
                                dist[i][j] = val
                                queue.append((val,(i,j)))
                
                
                queue = sorted(queue)
                
        return arr
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

# dfs technique