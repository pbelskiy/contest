/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int r_depth;
int r_val;

void dfs(struct TreeNode* node, int depth, bool left)
{
    if (!node)
        return;

    if (left && depth > r_depth) {
        r_val = node->val;
        r_depth = depth;
    }

    dfs(node->left, depth + 1, true);
    dfs(node->right, depth + 1, false || (node->left == NULL));
}

int findBottomLeftValue(struct TreeNode* root)
{
    r_val = root->val;
    r_depth = 0;

    dfs(root, 0, true);
    return r_val;
}
