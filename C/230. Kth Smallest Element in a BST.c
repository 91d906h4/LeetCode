/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int* vector;
int ptr;
void inorder(struct TreeNode* node) {
    if (node) {
        inorder(node->left);
        *(vector + ptr++) = node->val;
        inorder(node->right);
    }
}

int kthSmallest(struct TreeNode* root, int k){
    vector = (int*)malloc(10001 * sizeof(int));
    ptr = 0;

    inorder(root);

    return vector[k - 1];
}
