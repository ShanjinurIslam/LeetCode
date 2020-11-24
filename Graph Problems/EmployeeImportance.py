"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        graph = {}
        weight = {}
        visited = {}
        
        
        for each in employees:
            weight[each.id] = each.importance
            graph[each.id] = each.subordinates
            
        # bfs start
        
        queue = []
        queue.append(id)
        
        sum = 0
        
        while(len(queue)>0):
            u = queue.pop(0)
            
            if u in visited:
                continue
            else:
                visited[u] = True
                sum += weight[u]
                
            for v in graph[u]:
                if v in visited:
                    continue
                else:
                    queue.append(v)
        
        return sum