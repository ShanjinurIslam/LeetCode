class ListNode:
        def __init__(self,val=0,next=None,prev=None):
            self.val = val
            self.next = next
            self.prev = prev
        
class Solution(object):        
    def decrypt(self, code, k):
        head = None
        tail = head
        
        n = len(code)
        
        hash_map = {}
        
        for i,each in enumerate(code):
            if head == None:
                head = ListNode(each)
                tail = head
            else:
                prev = tail
                tail.next = ListNode(each)
                tail = tail.next
                tail.prev = prev
                
            hash_map[(i,each)] = tail
        
        tail.next = head
        head.prev = tail
        
        final = [0]*n
        
        if k>=0:
            for i in range(n):
                p = hash_map[(i,code[i])].next

                total = 0
                for _ in range(k):
                    total += p.val
                    p = p.next

                final[i] = total
        else:
            for i in range(n):
                p = hash_map[(i,code[i])].prev

                total = 0
                for _ in range(abs(k)):
                    total += p.val
                    p = p.prev

                final[i] = total
            
        return final
            
            
        
        
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        