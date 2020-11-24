# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def calculate_height(self,node,hash_map):
        if node == None:
            return 0
        else:
            hash_map[node] = 1 + max(self.calculate_height(node.left,hash_map),self.calculate_height(node.right,hash_map))
            return hash_map[node]
    
    def check_balanced(self,node,hash_map):
        if node == None:
            return True
        else:
            if node.left in hash_map:
                left = hash_map[node.left]
            else:
                left = 0
            if node.right in hash_map:
                right = hash_map[node.right]
            else:
                right = 0
            
            if abs(left-right) <= 1:
                return True and self.check_balanced(node.left,hash_map) and self.check_balanced(node.right,hash_map)
            else:
                return False
    
    
    def isBalanced(self, root):
        hash_map = {}
        self.calculate_height(root,hash_map)
        return self.check_balanced(root,hash_map)
        """
        :type root: TreeNode
        :rtype: bool
        """
        