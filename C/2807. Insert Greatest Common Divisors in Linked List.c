/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int _gcd (int a, int b) {
    if (a % b == 0)
        return b;
    else
        return _gcd(b, a % b);
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
    struct ListNode* current = head;

    while (current && current->next) {
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = _gcd(current->val, current->next->val);

        newNode->next = current->next;
        current->next = newNode;
        current = newNode->next;
    }

    return head;
}
