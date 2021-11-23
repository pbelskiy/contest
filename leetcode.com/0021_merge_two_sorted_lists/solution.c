struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    if (l1 && !l2)
        return l1;

    if (!l1 && l2)
        return l2;

    if (!l1 && !l2)
        return NULL;

    struct ListNode *head = malloc(sizeof(struct ListNode));
    struct ListNode *curr = head;

    while (l1 && l2) {
        if (l1->val < l2->val) {
            curr->val = l1->val;
            l1 = l1->next;
        } else {
            curr->val = l2->val;
            l2 = l2->next;
        }

        if (l1 && l2) {
            curr->next = malloc(sizeof(struct ListNode));
            curr = curr->next;
            curr->next = NULL;
            curr->val = -1;
        }
    }

    curr->next = (l1 == NULL) ? l2 : l1;
    return head;
}
