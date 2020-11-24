# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur_path(self,node,val):
        if node == None:
            return 
        if node.left == None and node.right == None:
            val = (val<<1) | (node.val)
            self.sum += val
            val = val >> 1
            return
        else:
            val = (val<<1) | (node.val)
            self.recur_path(node.left,val)
            self.recur_path(node.right,val)
            val = val >> 1
    
    def sumRootToLeaf(self, root):
        self.sum = 0
        self.recur_path(root,0)
        
        return self.sum
        
        
        """
        :type root: TreeNode
        :rtype: int
        """
        