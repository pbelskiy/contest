struct TreeNode *pruneTree(struct TreeNode *root)
{
    if (root->left && pruneTree(root->left) == NULL)
        root->left = NULL;

    if (root->right && pruneTree(root->right) == NULL)
        root->right = NULL;

    if (root->val == 0 && root->left == NULL && root->right == NULL)
        return NULL;

    return root;
}
