# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node,arr):
        if node == None:
            return
        
        self.inorder(node.left,arr)
        arr.append(node.val)
        self.inorder(node.right,arr)
    
    
    def minDiffInBST(self, root):
        a = []
        
        self.inorder(root,a)
        
        min_val = 10e10
        
        for i in range(len(a)-1):
            min_val = min(a[i+1] - a[i],min_val)
            
        return min_val
        
        """
        :type root: TreeNode
        :rtype: int
        """
        