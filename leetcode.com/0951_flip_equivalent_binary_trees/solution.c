/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool answer;

void solve(struct TreeNode* node1, struct TreeNode* node2)
{
    if (!answer)
        return;

    if ((node1 && !node2) || (!node1 && node2)) {
        answer = false;
        return;
    }

    if (node1 == NULL && node2 == NULL) {
        return;
    }

    /* same */
    if ( ((node1->left != NULL && node2->left != NULL && node1->left->val == node2->left->val) ||
          (node1->left == NULL && node2->left == NULL)) &&
         ((node1->right != NULL && node2->right != NULL && node1->right->val == node2->right->val) ||
          (node1->right == NULL && node2->right == NULL)) )
    {
        solve(node1->left, node2->left);
        solve(node1->right, node2->right);
        return;
    }

    /* flipped */
    if ( ((node1->left != NULL && node2->right != NULL && node1->left->val == node2->right->val) ||
          (node1->left == NULL && node2->right == NULL)) &&
        ((node1->right != NULL && node2->left != NULL && node1->right->val == node2->left->val) ||
         (node1->right == NULL && node2->left == NULL)) )
    {
        solve(node1->left, node2->right);
        solve(node1->right, node2->left);
        return;
    }

    /* not equal */
    answer = false;
}

bool flipEquiv(struct TreeNode* root1, struct TreeNode* root2)
{
    if (root1 && root2 && root1->val != root2->val)
        return false;

    answer = true;
    solve(root1, root2);
    return answer;
}
