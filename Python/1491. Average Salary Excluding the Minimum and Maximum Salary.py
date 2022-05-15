class Solution:
    def average(self, salary: List[int]) -> float:
#         salary.sort()
#         salary.pop()
#         salary.pop(0)
#         return sum(salary) / len(salary)

        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
