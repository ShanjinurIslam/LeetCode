# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.arr = []
    
    def inorder(self,node):
        if node == None:
            return
        
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)
    
    
    def increasingBST(self, root):
        self.arr = []
        self.inorder(root)
        
        if len(self.arr) == 0:
            return None
        else:
            node = None
            tail = None
            for each in self.arr:
                if node == None:
                    node = TreeNode(val=each,left=None,right=None)
                    tail = node
                else:
                    tail.right = TreeNode(val=each,left=None,right=None)
                    tail = tail.right
                
            return node
        