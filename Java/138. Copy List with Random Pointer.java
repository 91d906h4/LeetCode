/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public HashMap<Node, Node> nodes = new HashMap<Node, Node>();

    public Node dfs(Node node) {
            if (node == null) return null;
            if (nodes.containsKey(node)) return nodes.get(node);

            Node n = new Node(node.val);
            nodes.put(node, n);

            n.next = dfs(node.next);
            n.random = dfs(node.random);

            return n;
        }

    public Node copyRandomList(Node head) {
        return dfs(head);
    }
}
