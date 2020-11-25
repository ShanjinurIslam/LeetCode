# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,node,path):
        if node == None:
            return 0 
        elif node.left == None and node.right == None:
            if len(path) == 0:
                return 1
            else:
                if max(path) > node.val:
                    return 0
                else:
                    return 1
        else:
            if len(path) == 0:
                path.append(node.val)
                left = self.preorder(node.left,path)
                right = self.preorder(node.right,path)
                path.pop()
                
                return 1 + left + right
            else:
                if max(path) > node.val:
                    c = 0
                else:
                    c = 1
                    
                path.append(node.val)
                left = self.preorder(node.left,path)
                right = self.preorder(node.right,path)
                path.pop()
                
                return c + left + right
                
        
    
    def goodNodes(self, root):
        path = []
        
        return self.preorder(root,[])
        
        """
        :type root: TreeNode
        :rtype: int
        """
        