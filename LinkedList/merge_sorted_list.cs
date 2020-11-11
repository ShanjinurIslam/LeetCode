using System.Collections.Generic;
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
    private ListNode head;
    private ListNode temp;
    
    public Solution(){
        head = null;
        temp = head;
    }
    
    public void Insert(int val){
        if(head == null){
            head = new ListNode(val,null);
            temp = head ;
        }
        else{
            temp.next = new ListNode(val,null);
            temp = temp.next ;
        }
    }
    
    public ListNode MergeTwoLists(ListNode listNode1, ListNode listNode2) {
        List<int> list = new List<int>();

        while(listNode1 != null || listNode2 != null)
        {
            if (listNode1 == null && listNode2!=null)
            {
                list.Add(listNode2.val);
                listNode2 = listNode2.next;
            }
            else if(listNode2 == null && listNode1 != null)
            {
                list.Add(listNode1.val);
                listNode1 = listNode1.next;
            }
            else
            {
                if (listNode1.val <= listNode2.val)
                {
                    list.Add(listNode1.val);
                    list.Add(listNode2.val);
                }
                else
                {
                    list.Add(listNode2.val);
                    list.Add(listNode1.val);
                }

                listNode1 = listNode1.next;
                listNode2 = listNode2.next;
            }
        }

        list.Sort();

        for(int i = 0; i < list.Count; i++)
        {
            this.Insert(list[i]);
        }
        
        return this.head; 
    }
}