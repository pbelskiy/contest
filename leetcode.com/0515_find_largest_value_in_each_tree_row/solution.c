/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MAX(a,b) ((a > b ? a : b))

int *largestValues(struct TreeNode *root, int *returnSize)
{
    int *maxes = malloc(sizeof(int) * 100000);
    int count = 0;

    struct TreeNode *queue[1000];
    int qlen = 0;

    if (root)
        queue[qlen++] = root;

    // BFS
    while (qlen) {
        int row_max = queue[0]->val;
        struct TreeNode *new_queue[1000];
        int new_len = 0;

        for (int i = 0 ; i < qlen ; i++) {
            row_max = MAX(row_max, queue[i]->val);

            if (queue[i]->left)
                new_queue[new_len++] = queue[i]->left;

            if (queue[i]->right)
                new_queue[new_len++] = queue[i]->right;
        }

        qlen = 0;
        for (int i = 0 ; i < new_len ; i++)
            queue[qlen++] = new_queue[i];

        maxes[count++] = row_max;
    }

    *returnSize = count;
    return maxes;
}
