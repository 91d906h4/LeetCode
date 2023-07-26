# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        odd, temp = True, 0

        while queue:
            n = len(queue)

            for _ in range(n):
                v = queue.popleft()
                if v.left: queue.append(v.left)
                if v.right: queue.append(v.right)
                if v:
                    if odd:
                        if v.val % 2 == 0: return False
                        if temp < v.val: temp = v.val
                        else: return False
                    else:
                        if v.val % 2 == 1: return False
                        if temp > v.val: temp = v.val
                        else: return False

            odd = not odd
            temp = 0 if odd else float("inf")
                
        return True
