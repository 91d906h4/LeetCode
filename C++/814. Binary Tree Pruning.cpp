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
    bool ifOnes(TreeNode* node) {
        if(!node) return true;

        bool l = ifOnes(node->left), r = ifOnes(node->right);

        if(l) node->left = nullptr;
        if(r) node->right = nullptr;

        return node->val == 0 && l && r;
    }

    TreeNode* pruneTree(TreeNode* root) {
        return ifOnes(root) ? nullptr : root;
    }
};
