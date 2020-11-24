# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        level_wise_map = {}
        queue = []
        
        if root!=None:
            queue.append((0,root))
        
        while(len(queue)>0):
            level,node = queue.pop(0)
            
            if level in level_wise_map:
                level_wise_map[level].append(node.val)
            else:
                level_wise_map[level] = [node.val]
                
            if node.left != None:
                queue.append(((level+1),node.left))
            
            if node.right != None:
                queue.append(((level+1),node.right))
        
        return reversed(level_wise_map.values())
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        