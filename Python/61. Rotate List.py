# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        if not temp: return head

        k %= len(temp)

        while k:
            temp = [temp[-1]] + temp[:-1]
            k -= 1

        res = pointer = ListNode(temp[0])
        del temp[0]

        while temp:
            t = ListNode(temp[0])
            pointer.next = t
            pointer = t

            del temp[0]

        return res
