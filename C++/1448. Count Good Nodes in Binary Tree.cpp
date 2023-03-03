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
    int res = 0;

    void dfs(TreeNode* node, int m) {
        if(!node) return;

        if(node->val >= m) {
            res++;
            m = node->val;
        }

        if(node->left) dfs(node->left, m);
        if(node->right) dfs(node->right, m);
    }

    int goodNodes(TreeNode* root) {
        dfs(root, -10001);

        return res;
    }
};
