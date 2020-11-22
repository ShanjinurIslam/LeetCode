class Solution(object):
    class ListNode:
        def __init__(self,val):
            self.val = val
            self.next = None
            
    
    def sortArrayByParity(self, A):
        head = ListNode(A[0])
        tail = head
        
        for i in A[1:]:
            if i%2 == 0:
                new_node = ListNode(i)
                new_node.next = head
                head = new_node
            else:
                new_node = ListNode(i)
                tail.next = new_node
                tail = tail.next
        
        arr = []
        
        p = head
        
        while(p!=None):
            arr.append(p.val)
            p = p.next
                
        return arr
        
        
        
        """
        :type A: List[int]
        :rtype: List[int]
        """
        