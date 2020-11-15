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
    public int GetDecimalValue(ListNode head) {
        int sum = 0;
        ListNode temp = head;
        
        while(temp!=null){
            sum = (sum << 1) | temp.val ;
            temp = temp.next;
        }
        
        return sum;
    }
}