# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node,hash_map):
        if node == None:
            return
        else:
            self.inorder(node.left,hash_map)
            
            if node.val in hash_map:
                hash_map[node.val] += 1
            else:
                hash_map[node.val] = 1
                
            self.inorder(node.right,hash_map)
    
    def isUnivalTree(self, root):
        hash_map = {}
        
        self.inorder(root,hash_map)
        
        return True if len(hash_map.keys()) == 1 else False
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        