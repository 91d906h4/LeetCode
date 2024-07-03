/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int temp = 0;
    struct ListNode* t1 = l1;
    struct ListNode* t2 = l2;

    while (t1) {
        if (t1 && t2 && (!t1->next && t2->next)) {
            t1->next = t2->next;
            t2->next = NULL;
        }

        if (t2) {
            temp = temp + t1->val + t2->val;
            t1->val = temp % 10;
            temp /= 10;
            t1 = t1->next; t2 = t2->next;
        }
        else {
            temp = temp + t1->val;
            t1->val = temp % 10;
            temp /= 10;

            if (temp == 0) break;
            else if (!t1->next) {
                struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
                new_node->val = 1;
                new_node->next = NULL;
                temp = 0;

                t1->next = new_node;
                break;
            }
            else {
                t1 = t1->next;
            }
        }
    }

    if (temp) {
        t1 = l1;
        while (t1->next)
            t1 = t1->next;

        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = 1;
        new_node->next = NULL;

        t1->next = new_node;
    }

    return l1;
}
