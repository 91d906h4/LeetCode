/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// traversal: Traverse the sub-tree of root and calculate the sum and node number.
void traversal(struct TreeNode* root, int* result, int* count) {
    if (root->left) traversal(root->left, result, count);
    if (root->right) traversal(root->right, result, count);

    *result += root->val;
    *count += 1;
}

// subAvg: Calculate the average of the sub-tree of root.
int subAvg(struct TreeNode* root) {
    int result = 0, count = 0;

    traversal(root, &result, &count);

    return result / count;
}

// help: Iterate all the tree node in root.
void help(struct TreeNode* root, int* result) {
    if (root->left) help(root->left, result);
    if (root->right) help(root->right, result);

    if (root->val == subAvg(root))
        *result += 1;
}

int averageOfSubtree(struct TreeNode* root) {
    int result = 0;

    help(root, &result);

    return result;
}
