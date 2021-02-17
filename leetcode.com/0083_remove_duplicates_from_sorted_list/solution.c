/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode *curr = head;
        
    while (curr) {
        if (curr->next && curr->next->val == curr->val) {
            curr->next = curr->next->next;
        } else {
            curr = curr->next;
        }
    }
    
    return head;
}

