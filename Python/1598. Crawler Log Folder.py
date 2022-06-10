class Solution:
    def minOperations(self, logs: List[str]) -> int:
#         result = 0
#         for i in logs:
#             if i == "./": continue
#             elif i == "../": result -= 1
#             else: result +=1
#             result = max(result, 0)
#         return result

        result = []
        for i in logs:
            if i == "./": continue
            elif i == "../":
                if result: result.pop()
            else: result.append(i)
        return len(result)
