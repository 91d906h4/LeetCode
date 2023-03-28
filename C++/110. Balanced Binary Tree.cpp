/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int defth(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(defth(node->left), defth(node->right));
    }

    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        int l = defth(root->left), r = defth(root->right);
        return abs(l - r) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }
};
