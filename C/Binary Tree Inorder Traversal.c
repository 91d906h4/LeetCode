/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void inOrder(int* order, struct TreeNode* node, int* i) {
    if (node == NULL) return;

    inOrder(order, node->left, i);
    order[(*i)++] = node->val;
    inOrder(order, node->right, i);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
    int* order = (int*)malloc(100 * sizeof(int));
    *returnSize = 0;
    inOrder(order, root, returnSize);
    return order;
}
