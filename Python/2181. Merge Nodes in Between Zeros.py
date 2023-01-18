# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node.next.next:
                node.next = None
                return

            if node.next.val != 0:
                node.val += node.next.val
                node.next = node.next.next
                helper(node)
            else:
                helper(node.next)

        helper(head)

        return head
