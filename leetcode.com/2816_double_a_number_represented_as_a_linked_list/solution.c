int solve(struct ListNode *node)
{
    if (!node)
        return 0;

    int r = solve(node->next);
    int n = node->val*2 + r;

    node->val = n % 10;
    return n / 10;
}

struct ListNode *doubleIt(struct ListNode *head)
{
    int r = solve(head);
    if (r == 0)
        return head;

    struct ListNode *new_head = malloc(sizeof(struct ListNode));
    new_head->val = r;
    new_head->next = head;
    return new_head;
}
