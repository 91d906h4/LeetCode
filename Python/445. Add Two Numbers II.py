# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = 0, 0

        while l1:
            a *= 10
            a += l1.val
            l1 = l1.next

        while l2:
            b *= 10
            b += l2.val
            l2 = l2.next

        a += b
        a = list(str(a))
        res = pointer = ListNode(a[0])
        del a[0]

        while a:
            n = ListNode(a[0])
            del a[0]

            pointer.next = n
            pointer = n

        return res
