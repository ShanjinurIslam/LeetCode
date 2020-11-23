# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self,t1,t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return (t1.val==t2.val) and self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left)  
    
    def isSymmetric(self, root):
        if root == None:
            return True
        
        
        return self.isMirror(root.left,root.right)
        
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        