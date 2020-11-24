
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def construct(self,node,nums):
        n = len(nums)
        
        if n == 0:
            return
        
        mid = n/2
        node = TreeNode(nums[mid])
        
        node.left = self.construct(node.left,nums[:mid])
        if mid+1 < n:
            node.right = self.construct(node.right,nums[mid+1:])
            
        return node

    def sortedArrayToBST(self, nums):
        return self.construct(None,nums)
        
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        