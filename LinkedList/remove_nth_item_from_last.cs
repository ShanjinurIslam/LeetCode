public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n)
        {
            ListNode parent = null;
            ListNode p = head;

            List<Tuple<ListNode, ListNode>> parent_child_pairs = new List<Tuple<ListNode, ListNode>>();

            while (p != null)
            {
                parent_child_pairs.Add(new Tuple<ListNode, ListNode>(parent,p));
                parent = p;
                p = p.next; 
            }

            parent = parent_child_pairs[parent_child_pairs.Count - n].Item1;
            p = parent_child_pairs[parent_child_pairs.Count - n].Item2;
            
            if(parent == null){
                if(p.next == null){
                    return null;
                }
                else{
                    head = p.next;
                    return head;
                }
            }
            
            else{
                parent.next = p.next;
                 return head;
            }
           
        }
}