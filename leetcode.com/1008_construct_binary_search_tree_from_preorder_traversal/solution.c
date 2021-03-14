/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

inline void insert(struct TreeNode *root, int value)
{
    struct TreeNode *node = malloc(sizeof(struct TreeNode));

    node->val = value;
    node->left = NULL;
    node->right = NULL;

    while (root) {
        if (value > root->val) {
            if (root->right) {
                root = root->right;
            } else {
                root->right = node;
                break;
            }
        } else {
            if (root->left) {
                root = root->left;
            } else {
                root->left = node;
                break;
            }
        }
    }
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize)
{
    struct TreeNode *node = malloc(sizeof(struct TreeNode));

    node->val = preorder[0];
    node->left = NULL;
    node->right = NULL;

    for (int i = 1 ; i < preorderSize ; i++)
        insert(node, preorder[i]);

    return node;
}
