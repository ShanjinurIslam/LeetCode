"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def recur(self,node):
        if node == None:
            return 0
        else:
            max_val = 1
            for each in node.children:
                max_val = max(max_val,1 + self.recur(each))
                
            return max_val
    
    def maxDepth(self, root):
        return self.recur(root)
        """
        :type root: Node
        :rtype: int
        """
        