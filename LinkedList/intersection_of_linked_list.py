# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hash_map = {}
        
        p = headA
        
        while(p!=None):
            hash_map[p] = p
            p = p.next
            
        p = headB
        
        inter = None
        
        while(p!=None):
            if p in hash_map:
                inter = p
                break
            p = p.next
            
        return inter
        
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        