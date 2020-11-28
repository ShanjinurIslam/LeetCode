# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return []
        
        level_order = {}
        queue = []
        
        queue.append((root,0))
        
        while(len(queue)>0):
            node,level = queue.pop(0)
            
            if level in level_order:
                level_order[level].append(node.val)
                
            else:
                level_order[level] = [node.val]
                
            if node.left != None:
                queue.append((node.left,level+1))
            if node.right != None:
                queue.append((node.right,level+1))
                
        
        return [level_order[key][-1] for key in sorted(level_order.keys())]
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        