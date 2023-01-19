import numpy as np

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        drc, x, y = 0, 0, -1
        matrix = np.full((m, n), -1)

        while head:
            if drc == 0:
                if y + 1 < n and matrix[x][y + 1] == -1:
                    matrix[x][y + 1] = head.val
                    y += 1
                else:
                    drc = 1
                    continue
            elif drc == 1:
                if x + 1 < m and matrix[x + 1][y] == -1:
                    matrix[x + 1][y] = head.val
                    x += 1
                else:
                    drc = 2
                    continue
            elif drc == 2:
                if y - 1 >= 0 and matrix[x][y - 1] == -1:
                    matrix[x][y - 1] = head.val
                    y -= 1
                else:
                    drc = 3
                    continue
            elif drc == 3:
                if x - 1 >= 0 and matrix[x - 1][y] == -1:
                    matrix[x - 1][y] = head.val
                    x -= 1
                else:
                    drc = 0
                    continue
            head = head.next
        
        return matrix
