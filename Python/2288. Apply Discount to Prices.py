class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        temp = sentence.split()
        result = []
        for i, j in enumerate(temp):
            if match("\$\d+$", j):
                temp[i] = ("${:.2f}").format(int(j[1:]) * ((100 - discount) / 100))
        return " ".join(temp)
