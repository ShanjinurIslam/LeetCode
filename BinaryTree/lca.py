# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parent_map = {}
        node_map = {}
        
        queue = []
        
        queue.append(root)
        
        while(len(queue)>0):
            node = queue.pop(0)
            
            if not node.val in parent_map:
                parent_map[node.val] = -1
            
            node_map[node.val] = node
                
            if node.left != None:
                if not node.left.val in parent_map:
                    parent_map[node.left.val] = node.val
                queue.append(node.left)
                
            if node.right != None:
                if not node.right.val in parent_map:
                    parent_map[node.right.val] = node.val
                queue.append(node.right)
                
        
        path_p = []
        path_q = []
        
        def dfs_util(node,path):
            if parent_map[node] == -1:
                path.append(node)
                return
            
            else:
                path.append(node)
                dfs_util(parent_map[node],path)
        
        dfs_util(p.val,path_p)
        dfs_util(q.val,path_q)
        
        visited = {}
        
        for each in path_p:
            visited[each] = 1
            
        for each in path_q:
            if each in visited:
                return node_map[each]
        
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        