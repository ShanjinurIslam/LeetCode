# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,node):
        if node == None:
            return None
        
        prev = None
        curr = node
        
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    
    def gen_arr(self,node):
        arr = []
        p = node
        
        while(p!=None):
            arr.append(p.val)
            p = p.next
        
        return arr
        
    def isPalindrome(self, head):
        return self.gen_arr(head) == self.gen_arr(self.reverse(head))
        
        
        """
        :type head: ListNode
        :rtype: bool
        """
        