# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        temp = temp[:left - 1] + list(reversed(temp[left - 1: right])) + temp[right:]

        res = pointer = ListNode(temp[0])
        del temp[0]

        while temp:
            n = ListNode(temp[0])
            pointer.next = n
            pointer = n
            del temp[0]

        return res
