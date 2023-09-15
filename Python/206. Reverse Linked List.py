# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # if not head or not head.next: return head

      # before = head
      # head = head.next
      # before.next = None

      # while head.next:
      #   after = head.next
      #   head.next = before

      #   before = head
      #   head = after

      # head.next = before

      # return head

      before = None

      while head:
        after = head.next
        head.next = before
        before = head
        head = after

      return before
