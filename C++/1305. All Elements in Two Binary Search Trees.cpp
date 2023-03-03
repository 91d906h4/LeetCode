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
    vector<int> l;

    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        dfs(root1);
        dfs(root2);

        sort(l.begin(), l.end());

        return l;
    }

    void dfs(TreeNode* node) {
        if(node) l.push_back(node->val);
        else return;

        if(node->left) dfs(node->left);
        if(node->right) dfs(node->right);
    }
};
