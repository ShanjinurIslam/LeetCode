class Solution(object):
    def inorder(self,node,arr):
        if node == None:
            return
        self.inorder(node.left,arr)
        arr.append(node.val)
        self.inorder(node.right,arr)
    
    def isValidBST(self, root):
        arr = []
        self.inorder(root,arr)

        n = len(arr)
        
        for i in range(0,n-1):
            if arr[i] >= arr[i+1]:
                return False
        
        return True