"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.arr = []
    
    def pre_order(self,node):
        if node == None:
            return
        
        self.arr.append(node.val) 
        
        for each in node.children:
            self.pre_order(each)
        
    
    def preorder(self, root):
        self.arr = []
        self.pre_order(root)
        
        return self.arr
        """
        :type root: Node
        :rtype: List[int]
        """
        