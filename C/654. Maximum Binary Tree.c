/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {
    if (numsSize == 0) return NULL;

    int maxPtr = 0;

    for (int i = 0; i < numsSize; i++)
        if (nums[i] > nums[maxPtr])
            maxPtr = i;

	struct TreeNode* const newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));

    newNode->val = nums[maxPtr];
    newNode->left = constructMaximumBinaryTree(nums, maxPtr);
    newNode->right = constructMaximumBinaryTree(nums + maxPtr + 1, numsSize - maxPtr - 1);

    return newNode;
}
