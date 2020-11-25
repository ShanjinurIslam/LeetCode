# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self,node,parent):
        if node == None:
            return 0
        if node.left == None and node.right == None and parent == None:
            return 0
        elif node.left == None and node.right == None and parent.left == node:
            return node.val
        else:
            return self.traverse(node.left,node) + self.traverse(node.right,node)
    
    def sumOfLeftLeaves(self, root):
        return self.traverse(root,None)
        
        """
        :type root: TreeNode
        :rtype: int
        """
        