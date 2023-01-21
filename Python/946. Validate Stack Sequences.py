class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        while popped != []:
            if stack == [] or popped[0] != stack[-1]:
                if popped[0] in stack: return False
                else: stack.append(pushed.pop(0))
            else:
                stack.pop()
                popped.pop(0)
        
        return True
