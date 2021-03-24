/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitListToParts(struct ListNode* root, int k, int* returnSize)
{
    int length = 0;

    for (struct ListNode *node = root ; node ; length++)
        node = node->next;

    int chunk_size = length / k;
    int chunk_count = length % k;

    printf("length = %d ; %d, %d\n", length, chunk_size, chunk_count);

    struct ListNode *node = root;
    struct ListNode** splitted = calloc(sizeof(struct ListNode*), k);

    for (int i = 0 ; i < k ; i++)
    {
        struct ListNode *sl = NULL;
        struct ListNode *prev = NULL;

        for (int j = 0 ; node && j < chunk_size + (chunk_count > 0) ? 1 : 0 ; j++, chunk_count--)
        {
            struct ListNode *e = malloc(sizeof(struct ListNode));
            e->val = node->val;
            e->next = NULL;

            if (sl == NULL)
                sl = e;

            if (prev != NULL)
                prev->next = e;

            prev = e;
            node = node->next;
        }

        splitted[i] = sl;
    }

    *returnSize = k;
    return splitted;
}
