class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *current_node;
        ListNode *prev_node;
        ListNode *next_node;

        prev_node = NULL;
        current_node = head;

        while (current_node != NULL)
        {
            next_node = current_node->next;
            current_node->next = prev_node;
            prev_node = current_node;
            current_node = next_node;
        }

        head = prev_node;
        
        return head;
    }
};
