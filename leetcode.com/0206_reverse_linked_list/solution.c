struct ListNode *reverse(struct ListNode *parent, struct ListNode *current)
{
    if (current == NULL)
        return parent;

    struct ListNode *head = reverse(current, current->next);
    current->next = parent;
    parent->next = NULL;
    return head;
}

struct ListNode *reverseList(struct ListNode *head)
{
    if (head == NULL)
        return NULL;

    return reverse(head, head->next);
}
