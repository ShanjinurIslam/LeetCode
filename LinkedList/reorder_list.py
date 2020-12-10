# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if head == None:
            return
        
        n = 0
        
        p = head
        arr = []
        
        
        while(p!=None):
            arr.append(p)
            p = p.next
            n += 1
        
        forward = 1
        backward = n-1
        turn = 1
        
        p = head
        
        for _ in range(1,n):
            if turn % 2 == 0:
                p.next = arr[forward]
                p = p.next
                forward += 1
            else:
                p.next = arr[backward]
                p = p.next
                backward -= 1
            
            turn += 1
        
        p.next = None
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        