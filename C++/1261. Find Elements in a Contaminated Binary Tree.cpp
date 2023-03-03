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
class FindElements {
public:
    set<int> s;

    void dfs(TreeNode* node) {
        if(!node) return;

        if(node->left){
            node->left->val = node->val * 2 + 1;
            s.insert(node->left->val);
            dfs(node->left);
        }
        if(node->right){
            node->right->val = node->val * 2 + 2;
            s.insert(node->right->val);
            dfs(node->right);
        }
    }

    FindElements(TreeNode* root) {
        root->val = 0;
        s.insert(0);
        dfs(root);
    }
    
    bool find(int target) {
        return s.count(target);
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
