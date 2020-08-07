class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        count = 0
        
        while l1 is not None:
            val1 += l1.val *pow(10,count) 
            l1 = l1.next
            count += 1
        
        val2 = 0
        count = 0
        
        while l2 is not None:
            val2 += l2.val * pow(10,count)
            l2 = l2.next
            count += 1
            
        total = int(val1 + val2)
        out = ListNode()
        curr = out

        while total != 0:
            curr.val = total%10
            total = total // 10
            if total != 0:
                curr.next = ListNode()
                curr = curr.next
            else:
                curr.next = None
            
        return out

if __name__ == "__main__":
    val1 = [2,4,3]
    val2 = [5,6,4]

    l1 = ListNode()
    curr = l1

    for i in range(len(val1)):
        curr.val = val1[i]
        if i==len(val1)-1:
            curr.next = None
            break
        else:
            curr.next = ListNode()
            curr = curr.next

    l2 = ListNode()
    curr = l2

    for i in range(len(val2)):
        curr.val = val2[i]
        if i==len(val2)-1:
            curr.next = None
            break
        else:
            curr.next = ListNode()
            curr = curr.next

    s = Solution()
    r = s.addTwoNumbers(l1,l2)

    while r is not None:
        print(r.val)
        r = r.next