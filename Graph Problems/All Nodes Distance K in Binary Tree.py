# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,node,adjList):
        if node == None:
            return
        
        self.inorder(node.left,adjList)
        adjList[node.val] = []
        self.inorder(node.right,adjList)
    
    def distanceK(self, root, target, K):
        adjList = {}
        
        self.inorder(root,adjList)
        
        queue = []
        
        queue.append(root)
        
        while(len(queue)>0):
            node = queue.pop(0)
                
            if node.left != None:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                queue.append(node.left)
            
            if node.right != None:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                queue.append(node.right)
                
        dist = {}
        visited = {}
        
        for each in adjList.keys():
            dist[each] = -10e9
            visited[each] = False
        start = target.val 
        dist[start] = 0
        arr = set()
        
        queue = []
        queue.append(start)
        
        
        while(len(queue)>0):
            u = queue.pop(0)
            
            if dist[u] == K:
                arr.add(u)
            
            if visited[u]:
                continue
            
            else:
                visited[u] = True
                for v in adjList[u]:
                    if not visited[v]:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        
           
        return list(arr)
        
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        