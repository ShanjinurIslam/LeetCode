# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur(self,node):
        if node == None:
            return 0
        else:
            if node.left == None:
                return 1 + self.recur(node.right)
            elif node.right == None:
                return 1 + self.recur(node.left)
            else:
                return 1 + min(self.recur(node.left),self.recur(node.right))
    
    def minDepth(self, root):
        return self.recur(root)
        """
        :type root: TreeNode
        :rtype: int
        """
        