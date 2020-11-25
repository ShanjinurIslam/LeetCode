# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node,arr):
        if node == None:
            return 
        
        self.inorder(node.left,arr)
        arr.append(node.val)
        self.inorder(node.right,arr)
    
    
    def getMinimumDifference(self, root):
        arr = []
        
        self.inorder(root,arr)
        
        min_val = abs(arr[0] - arr[1])
        
        n = len(arr)
        
        for i in range(1,n-1):
            min_val = min(min_val,abs(arr[i] - arr[i+1])) 
            
        return min_val
        
        """
        :type root: TreeNode
        :rtype: int
        """
        