# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = []

        # while head:
        #     temp.append(head.val)
        #     head = head.next

        # temp[k - 1], temp[-k] = temp[-k], temp[k - 1]

        # res = pointer = ListNode(temp[0])
        # del temp[0]

        # for i in temp:
        #     n = ListNode(i)
        #     pointer.next = n
        #     pointer = n

        # return res

        temp, t = [], head

        while t: temp.append(t); t = t.next

        temp[k - 1].val, temp[-k].val = temp[-k].val, temp[k - 1].val

        return head
