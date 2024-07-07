/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * 2);
    Node* head = malloc(sizeof(Node));
    Node* ptr = head;
    Node* tail = head;

    head->key = -197137; // Magic number 197137 is a prime number.
    head->value = -197137;
    head->next = NULL;

    for (int i = 0; i < numsSize; i++) {
        int temp = *(nums + i);
        ptr = head;

        while (ptr) {
            if (ptr->key == target - temp) {
                *(result + 0) = i;
                *(result + 1) = ptr->value;
                *returnSize = 2;
                return result;
            }
            ptr = ptr->next;
        }

        Node* newNode = malloc(sizeof(Node));
        newNode->key = temp;
        newNode->value = i;
        newNode->next = NULL;

        tail->next = newNode;
        tail = newNode;
    }

    *returnSize = 0;
    return result;
}
