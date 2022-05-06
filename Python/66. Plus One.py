class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = "".join(map(str, digits))
        a = int(a) + 1
        b = list(str(a))
        return b
