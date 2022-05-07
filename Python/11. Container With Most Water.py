class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        xmax = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            xmax = max(area, xmax)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return xmax
