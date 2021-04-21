/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool hasPathSum(struct TreeNode* root, int targetSum)
{
    if (root == NULL)
        return false;

    if (root->left == NULL && root->right == NULL) {
        targetSum -= root->val;

        if (targetSum == 0)
            return true;

        return false;
    }

    if (hasPathSum(root->left, targetSum - root->val))
        return true;

    if (hasPathSum(root->right, targetSum - root->val))
        return true;

    return false;
}
