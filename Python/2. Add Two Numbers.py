# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        overflow = 0

        while l1 or l2 or overflow != 0:
            temp = overflow
            if l1: temp += l1.val
            if l2: temp += l2.val

            cur.val = temp % 10
            overflow = temp // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if not (l1 or l2 or overflow != 0): break

            next = ListNode()
            cur.next = next
            cur = next

        return res
