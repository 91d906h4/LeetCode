# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    carry = 0

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if node.next:
                dfs(node.next)

            temp = node.val * 2 + self.carry

            node.val = temp % 10
            self.carry = temp // 10

        dfs(head)

        # Check if carry
        if self.carry != 0:
            new = ListNode(
                val=self.carry,
                next=head,
            )
        else:
            new = head

        return new
