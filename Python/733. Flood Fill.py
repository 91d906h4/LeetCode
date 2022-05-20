class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        w, h = len(image), len(image[0])
        origin = image[sr][sc]
        def dfs(x, y):
            if not (0 <= x < w) or not (0 <= y < h):
                return image
            if image[x][y] == origin:
                image[x][y] = newColor
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
        
        dfs(sr, sc)
        return image
