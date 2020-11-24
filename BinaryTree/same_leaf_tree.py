# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 16ms Solution
class Solution(object):
    def get_all_leaves(self,node):
        if node == None:
            return []
        elif node.left == None and node.right == None:
            return [node.val]
        else:
            arr = []
            arr.extend(self.get_all_leaves(node.left))
            arr.extend(self.get_all_leaves(node.right))
            return arr
    
    
    def leafSimilar(self, root1, root2):
        return self.get_all_leaves(root1)==self.get_all_leaves(root2)
        
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        