# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max = -10e10
    
    def get_paths(self,node,path): # preorder traversal
        n = len(path)
        
        if node == None:
            return
        
        elif node.left == None and node.right == None:
            if(n>=1):
                for i in range(n):
                    if self.max < abs(node.val-path[i]):
                        self.max = abs(node.val-path[i])
            return
        else:
            if(n>=1):
                for i in range(n):
                    if self.max < abs(node.val-path[i]):
                        self.max = abs(node.val-path[i])
                
            path.append(node.val)
                
            self.get_paths(node.left,path)
            self.get_paths(node.right,path)
            path.pop()
            
            return
    
    def maxAncestorDiff(self, root):
        path = []
        
        self.get_paths(root,path)
        
        return self.max
        
        """
        :type root: TreeNode
        :rtype: int
        """
        