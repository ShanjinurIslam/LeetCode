class Solution(object):
    def makeConnected(self, n, connections):
        adjList = []
        for each in range(n):
            adjList.append([])
            
        edges = len(connections)
        
        if(edges<n-1):
            return -1
        
        for edge in connections:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = [False]*n
        
        def dfs(node):
            if visited[node]:
                return 0
            else:
                visited[node] = True
                for each in adjList[node]:
                    dfs(each)
                return 1
        
        '''
        queue = []
        
        queue.append(0)
        total_visited = 0
        
        while(len(queue)>0):
            u = queue.pop(0)
            
            if visited[u]:
                continue
            else:
                visited[u] = True
                total_visited += 1
                
                for v in adjList[u]:
                    if not visited[v]:
                        queue.append(v)
        '''
        
        return sum(dfs(i) for i in range(n)) - 1
        
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        