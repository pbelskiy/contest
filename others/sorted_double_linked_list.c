#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LENGTH  5

typedef struct Node {
    struct Node *prev;
    struct Node *next;
    int value;
} Node;

Node* generate()
{
    Node *head, *last = NULL;

    srand(0);

    for (int i = 0 ; i < LENGTH ; i++) {
        Node *curr = malloc(sizeof(Node));

        if (i == 0)
            head = curr;

        curr->value = rand() % 100;
        curr->prev = last;
        curr->next = NULL;

        if (last)
            last->next = curr;

        last = curr;
    }

    return head;
}

Node* bubble_sort(Node *head)
{
    bool sorted = false;

    while (!sorted) {
        sorted = true;
        Node *curr = head;

        while (curr) {
            /* swap */
            if (curr->next && curr->value > curr->next->value) {
                Node *n0 = (curr->prev == NULL) ? NULL : curr->prev;
                Node *n1 = curr;
                Node *n2 = curr->next;
                Node *n3 = (n2->next == NULL) ? NULL : n2->next;

                if (n0)
                    n0->next = n2;

                n2->prev = n0;
                n2->next = n1;

                n1->prev = n2;
                n1->next = n3;

                if (n3)
                    n3->prev = n1;

                if (n1 == head)
                    head = n2;

                sorted = false;
            }

            curr = curr->next;
        }
    }

    return head;
}

void check(Node *head)
{
    Node *tail;
    int prev = head->value;

    /* head to tail */
    while (head) {
        printf("%d ", head->value);

        // if (head->value < prev)
        //     printf("[!] ");

        prev = head->value;

        if (head->next == NULL) {
            tail = head;
            break;
        } else {
            head = head->next;
        }
    }
    printf("\n");

    /* tail to head */
    while (tail) {
        printf("%d ", tail->value);

        // if (tail->value > prev)
        //     printf("[!] ");

        prev = tail->value;
        tail = tail->prev;
    }
    printf("\n");
}

int main()
{
    Node *head = generate();

    head = bubble_sort(head);
    check(head);
    return 0;
}
