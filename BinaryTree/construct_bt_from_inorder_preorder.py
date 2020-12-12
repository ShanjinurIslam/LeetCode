class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object): 
    def recur(self,preorder,inorder):
        n = len(inorder)
        
        if n == 0:
            return None
        
        val = preorder.pop(0)
        node = TreeNode(val)
        try:
            index = inorder.index(val)
            if index > 0:
                node.left = self.recur(preorder,inorder[0:index])
            if index < n-1:
                node.right = self.recur(preorder,inorder[index+1:])
            return node
        except ValueError:
            return node
    def buildTree(self, preorder, inorder):
        return self.recur(preorder,inorder)
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        