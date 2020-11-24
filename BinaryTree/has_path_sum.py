# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse_path(self,node,path,sum):
        if node == None:
            return
        
        if node.left == None and node.right == None:
            path += node.val
            
            if path == sum:
                self.flag = True
            
            path -= node.val
        else:
            path += node.val
            
            self.traverse_path(node.left,path,sum)
            self.traverse_path(node.right,path,sum)
            path -= node.val
    
    
    def hasPathSum(self, root, sum):
        self.flag = False
        
        self.traverse_path(root,0,sum)
        
        return self.flag
        
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        