#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode *begin, *curr, *prev;
    int target = -101;

    begin = head;
    curr = head;
    prev = NULL;

    while (curr) {

        /* find duplications */
        if (curr->next && curr->next->val == curr->val)
            target = curr->val;

        if (curr->val != target) {
            prev = curr;
            curr = curr->next;
            continue;
        }

        /* remove all nodes with target value */
        while (curr && curr->val == target) {

            if (curr == begin) {
                begin = curr->next;
                curr = begin;
            } else {
                prev->next = curr->next;
                curr = curr->next;
            }
        }
    }

    return begin;
}
