/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        if(head == null){
            return head;
        }
        
        ListNode prev = null;
            ListNode p = head;

            while (p != null)
            {
                if (prev == null)
                {
                    prev = p;
                    p = p.next;
                }
                else
                {
                    if (prev.val == p.val)
                    {
                        p = p.next;
                    }
                    else
                    {
                        prev.next = p;
                        prev = p;
                        p = p.next;
                    }
                }
            }
        
            if(prev!=null){
                prev.next = null;
            }
        
        return head;
    }
}