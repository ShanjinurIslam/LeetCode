# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEqual(self,t1,t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return (t1.val==t2.val) and self.isEqual(t1.left,t2.left) and self.isEqual(t1.right,t2.right)  
        
    
    def isSameTree(self, p, q):
        return self.isEqual(p,q)
    
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        