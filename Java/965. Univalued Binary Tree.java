/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private boolean dfs(TreeNode root, TreeNode node){
        if(node == null) return true;

        if(node.val != root.val) return false;
        else return dfs(root, node.left) && dfs(root, node.right);
    }

    public boolean isUnivalTree(TreeNode root) {
        return dfs(root, root);
    }
}
