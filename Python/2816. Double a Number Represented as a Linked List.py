# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self) -> None:
        self.carry = 0

    def dfs(self, node: Optional[ListNode]) -> None:
        if node.next:
            self.dfs(node.next)

        temp = node.val * 2 + self.carry

        node.val = temp % 10
        self.carry = temp // 10

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dfs(head)

        # Check if carry
        if self.carry != 0:
            return ListNode(
                val=self.carry,
                next=head,
            )

        return head
