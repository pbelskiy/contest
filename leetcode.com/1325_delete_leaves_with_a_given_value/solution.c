bool dfs(struct TreeNode *node, int target)
{
    if (node == NULL)
        return false;

    if (node->left == NULL && node->right == NULL)
        return node->val == target;

    if (dfs(node->left, target))
        node->left = NULL;

    if (dfs(node->right, target))
        node->right = NULL;

    return node->left == NULL && node->right == NULL && node->val == target;
}

struct TreeNode *removeLeafNodes(struct TreeNode *root, int target)
{
    if (dfs(root, target))
        return NULL;

    return root;
}
