#include <stddef.h>
#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

unsigned int result = 0;

void print(unsigned int v)
{
    unsigned int i, s = 1 << ((sizeof(v) << 3) - 1);
    for (i = s; i; i >>= 1)
        printf("%d", v & i || 0);

    printf("\n");
}

void dfs(struct TreeNode* node, int depth, unsigned int sum)
{
    if (node == NULL)
        return;

    unsigned int next = sum | (
        (unsigned int) node->val << (sizeof(unsigned int) * 8 - depth - 1)
    );

    if (node->left == NULL && node->right == NULL) {
        next >>= (sizeof(unsigned int) * 8 - depth - 1);
        result += next;
        return;
    }

    dfs(node->left, depth + 1, next);
    dfs(node->right, depth + 1, next);
}

int sumRootToLeaf(struct TreeNode* root)
{
    dfs(root, 0, 0);
    return result;
}

int main()
{
    struct TreeNode ln1  = {0, NULL, NULL};
    struct TreeNode rn1  = {1, NULL, NULL};
    struct TreeNode rln  = {0, &ln1, &rn1};

    struct TreeNode ln2  = {0, NULL, NULL};
    struct TreeNode rn2  = {1, NULL, NULL};
    struct TreeNode rrn  = {1, &ln2, &rn2};

    struct TreeNode root = {1, &rln, &rrn};

    printf("sum = %d\n", sumRootToLeaf(&root));
    return 0;
}
