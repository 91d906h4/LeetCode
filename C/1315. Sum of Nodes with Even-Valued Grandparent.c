/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int result;

void helper(struct TreeNode* root, bool valid) {
    if (root->left) {
        if (root->left->left)
            helper(root->left->left, (root->val % 2 == 0));
        if (root->left->right)
            helper(root->left->right, (root->val % 2 == 0));
    }

    if (root->right) {
        if (root->right->left)
            helper(root->right->left, (root->val % 2 == 0));
        if (root->right->right)
            helper(root->right->right, (root->val % 2 == 0));
    }

    if (root && valid) {
        result += root->val;
    }
}
int sumEvenGrandparent(struct TreeNode* root) {
    result = 0;

    if (root) helper(root, 0);
    if (root->left) helper(root->left, 0);
    if (root->right) helper(root->right, 0);

    return result;
}
