# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.arr = []
    
    def recur_path(self,node,path):
        if node == None:
            return 
        if node.left == None and node.right == None:
            path.append(node.val)
            path_str = ""
            for each in path[:-1]:
                path_str += str(each) + "->"
            path_str += str(path[-1])
            self.arr.append(path_str)
            path.pop()
            return
        else:
            path.append(node.val)
            self.recur_path(node.left,path)
            self.recur_path(node.right,path)
            path.pop()
            
    
    def binaryTreePaths(self, root):
        path = []
        self.arr = []
        self.recur_path(root,path)
        return self.arr
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        