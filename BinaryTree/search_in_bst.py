# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.target = None
    
    def recur(self,node,val):
        if node == None:
            return 
        elif node.val == val:
            self.target = node
            return 
        else:
            self.recur(node.left,val)
            self.recur(node.right,val)
    
    def searchBST(self, root, val):
        self.recur(root,val)
        return self.target