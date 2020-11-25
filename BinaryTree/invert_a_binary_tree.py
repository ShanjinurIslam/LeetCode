# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invert(self,node):
        if node == None:
            return
        
        if node.left == None and node.right == None:
            return node
        
        temp = node.left
        node.left = self.invert(node.right)
        node.right = self.invert(temp)
        
        return node
        
    
    def invertTree(self, root):
        return self.invert(root)
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        