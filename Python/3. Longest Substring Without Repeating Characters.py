class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        dict_ = deque()
        i = 0
        while i < len(s):
            element = s[i]
            if element in dict_:
                dict_.popleft()
            else:
                dict_.append(element)
                i += 1
            result = max(result, len(dict_))
        return result
