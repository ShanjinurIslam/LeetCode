# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        hash_map = {}
        p = head
        
        while(p!=None):
            if p in hash_map:
                return hash_map[p]
            else:
                hash_map[p] = p
            
            p = p.next
            
        return None
        """
        :type head: ListNode
        :rtype: ListNode
        """
        