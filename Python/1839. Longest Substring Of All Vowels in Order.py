class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(set(word)) <= 4: return 0

        word += 'z'
        res, counter, pointer, temp = 0, 1, word[0], word[0]
        dict_ = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'x'}

        for i in word[1:]:
            if i == pointer: counter += 1; temp += i
            elif i == dict_[pointer]:
                pointer = i
                counter += 1; temp += i
            else:
                if pointer == 'u' and len(set(temp)) == 5: res = max(res, counter)
                counter = 1
                pointer = i
                temp = i

        return res
