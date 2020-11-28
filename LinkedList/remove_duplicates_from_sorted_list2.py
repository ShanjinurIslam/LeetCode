# O(nlogn) solution with Extra Memory

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        hash_map = {}
        
        p = head 
        
        while(p!=None):
            if p.val in hash_map:
                hash_map[p.val] += 1
            else:
                hash_map[p.val] = 1
                
            p = p.next
            
        
        final = None
        tail = None
        
        for key in sorted(hash_map.keys()):
            if hash_map[key] == 1:
                if final == None:
                    final = ListNode(key)
                    tail = final
                else:
                    tail.next = ListNode(key)
                    tail = tail.next
                    
        return final
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        