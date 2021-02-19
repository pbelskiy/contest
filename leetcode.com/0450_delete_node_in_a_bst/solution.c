#include <stdio.h>
#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void solve(struct TreeNode *curr, struct TreeNode **prev, int key)
{
    if (!curr)
        return;

    /* traverse left subtree */
    if (curr->val > key) {
        return solve(curr->left, &curr->left, key);
    }

    /* traverse right subtree */
    if (curr->val < key) {
        return solve(curr->right, &curr->right, key);
    }

    /* no children */
    if (!(curr->left || curr->right)) {
        *prev = NULL;
        return;
    }

    /* both children */
    if (curr->left && curr->right) {

        /* find minimal value of right subtree */
        struct TreeNode *rst = curr->right;

        while (rst) {
            if (!rst->left) {
                solve(curr, &curr->right , rst->val);
                curr->val = rst->val;
                break;
            }

            rst = rst->left;
        }

        return;
    }

    /* one of child */
    if (curr->left) {
        *prev = curr->left;
    } else {
        *prev = curr->right;
    }
}

struct TreeNode* deleteNode(struct TreeNode* root, int key)
{
    if (!root)
        return NULL;

    solve(root, &root, key);
    return root;
}

int main()
{
    struct TreeNode v7 = { .left = NULL, .right = NULL, .val = 7 };
    struct TreeNode v6 = { .left = NULL, .right = &v7,  .val = 6 };

    struct TreeNode v2 = { .left = NULL, .right = NULL, .val = 2 };
    struct TreeNode v4 = { .left = NULL, .right = NULL, .val = 4 };
    struct TreeNode v3 = { .left = &v2,  .right = &v4,  .val = 3 };

    struct TreeNode v5 = { .left = &v3,  .right = &v6,  .val = 5 };

    struct TreeNode *root = deleteNode(&v5, 5);

    return 0;
}

// [50,30,70,null,40,60,80]
// 50
// [0]
// 0
// [5,3,6,2,4,null,7]
// 5
// [5,3,6,2,4,null,7]
// 3
// [5,3,6,2,4,null,7]
// 0
// []
// 0
