"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.arr = []
    
    def post_order(self,node):
        if node == None:
            return
        
        for each in node.children:
            self.post_order(each)
        
        self.arr.append(node.val) 
    
    def postorder(self, root):
        self.arr = []
        self.post_order(root)
        
        return self.arr
        """
        :type root: Node
        :rtype: List[int]
        """
        