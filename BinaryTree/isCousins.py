# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        queue = []
        
        hash_map = {}
        queue.append((root,None,0))
        
        while(len(queue)>0):
            node,parent,level = queue.pop(0)
            
            hash_map[node.val] = (parent,level)
            
            if node.left !=None:
                queue.append((node.left,node,level+1))
            if node.right !=None:
                queue.append((node.right,node,level+1))
                
        
        node_x = hash_map[x]
        node_y = hash_map[y]
        
        if node_x[0]!=node_y[0] and node_x[1] == node_y[1]:
            return True
        else:
            return False
        
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        