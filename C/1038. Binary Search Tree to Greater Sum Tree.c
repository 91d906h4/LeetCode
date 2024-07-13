/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int temp;

struct TreeNode* help(struct TreeNode* root) {
    if (root->right) help(root->right);

    temp += root->val;
    root->val = temp;

    if (root->left) help(root->left);

    return root;
}

struct TreeNode* bstToGst(struct TreeNode* root) {
    temp = 0;

    return help(root);
}
