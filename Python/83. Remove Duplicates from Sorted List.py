# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hoge = head
        while hoge and hoge.next:
            if hoge.val == hoge.next.val: hoge.next = hoge.next.next
            else: hoge = hoge.next
        return head
