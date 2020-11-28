# 72ms
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        final = None
        tail = None
        p = head
        
        while(p!=None):
            if p.val == val:
                pass
            else:
                if final == None:
                    final = ListNode(p.val)
                    tail = final
                else:
                    tail.next = ListNode(p.val)
                    tail = tail.next
            
            p = p.next
                    
        
        return final
        

# Version 2 68ms No extra Node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return None
        
        while head.val == val:
            head = head.next
            if head == None:
                break
        
        prev = head
        p = None
        if head!=None:
            p = head.next
        
        while(p!=None):
            if p.val != val:
                prev.next = p
                prev = p
                p = p.next
            else:
                p = p.next
                
        if prev!=None:
            prev.next = None
        
        return head
        
        
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        