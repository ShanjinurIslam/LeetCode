# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length = 0
        p = head
        arr = []
        
        while p!= None:
            arr.append(p)
            p = p.next
            length += 1 
        
        if length == 1:
            return arr[0]
        
        else:
            return arr[(length)/2]
        