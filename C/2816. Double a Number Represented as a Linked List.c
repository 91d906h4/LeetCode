/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int carry;

void dfs(struct ListNode* node) {
    if (node->next)
        dfs(node->next);

    int temp = node->val * 2 + carry;

    node->val = temp % 10;
    carry = (int)(temp / 10);
}

struct ListNode* doubleIt(struct ListNode* head) {
    carry = 0;

    dfs(head);

    if (carry) {
        struct ListNode* new = malloc(sizeof(struct ListNode));

        new-> val = carry;
        new->next = head;

        return new;
    }

    return head;
}
