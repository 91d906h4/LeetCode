/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int compare(int* a, int* b) {
    if (*a == *b) return 0;
    else if (*a < *b) return -1;
    else return 1;
}

struct ListNode* sortList(struct ListNode* head) {
    int len = 0;
    struct ListNode* temp = head;

    while (temp) {
        len++;
        temp = temp->next;
    }

    int* list = (int*)malloc(sizeof(int) * len);
    temp = head;

    for (int i = 0; i < len; i++) {
        *(list + i) = temp->val;
        temp = temp->next;
    }

    qsort(list, len, sizeof(int), compare);

    temp = head;

    for (int i = 0; i < len; i++) {
        temp->val = *(list + i);
        temp = temp->next;
    }

    free(list);

    return head;
}
