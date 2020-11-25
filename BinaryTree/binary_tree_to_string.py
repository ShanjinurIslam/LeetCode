# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,node):
        if node == None:
            return ""
        elif node.left == None and node.right == None:
            return str(node.val)
        else:
            string = str(node.val)
            if node.left == None:
                string += "()"
            else:
                string += "(" + self.preorder(node.left) + ")"
            
            if node.right != None:
                string += "(" + self.preorder(node.right) + ")"
            return string
    
    
    def tree2str(self, t):
        return self.preorder(t)
        """
        :type t: TreeNode
        :rtype: str
        """
        