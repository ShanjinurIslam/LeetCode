# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recur(self,t1,t2):
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        else:
            return TreeNode(t1.val+t2.val,left=self.recur(t1.left,t2.left),right=self.recur(t1.right,t2.right))
    
    def mergeTrees(self, t1, t2):
        node = self.recur(t1,t2)
        return node
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        