struct ListNode *middleNode(struct ListNode* head)
{
    struct ListNode *fast = head;
    struct ListNode *slow = head;

    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow;
}
