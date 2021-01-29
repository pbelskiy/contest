#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode* root = (struct ListNode*) calloc(1, sizeof(struct ListNode));
    struct ListNode* last = root;
    int carry = 0;

    while (l1 || l2) {
        if (l1 && l2) {
            int sum = l1->val + l2->val + carry;
            last->val = sum % 10;
            carry = sum / 10;

            l1 = l1->next;
            l2 = l2->next;
        } else if (l1) {
            int sum = l1->val + carry;
            last->val = sum % 10;
            carry = sum / 10;

            l1 = l1->next;
        } else if (l2) {
            int sum = l2->val + carry;
            last->val = sum % 10;
            carry = sum / 10;

            l2 = l2->next;
        }

        if (l1 || l2) {
            last->next = (struct ListNode*) calloc(1, sizeof(struct ListNode));
            last = last->next;
        }
    }

    while (carry) {
        last->next = (struct ListNode*) calloc(1, sizeof(struct ListNode));
        last = last->next;
        last->val = carry % 10;
        carry = carry / 10;
    }

    return root;
}

int main()
{
    struct ListNode *r;
    struct ListNode l1[] = {
        { .val = 2, .next = &l1[1] },
        { .val = 4, .next = &l1[2] },
        { .val = 3, .next = NULL   },
    };

    struct ListNode l2[] = {
        { .val = 5, .next = &l2[1] },
        { .val = 6, .next = &l2[2] },
        { .val = 4, .next = NULL   },
    };

    r = addTwoNumbers(&l1[0], &l2[0]);

    printf("[ ");
    while (r) {
        printf("%d, ", r->val);
        r = r->next;
    }
    printf("]\n");

    return 0;
}
