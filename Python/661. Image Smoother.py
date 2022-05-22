class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ximg = copy.deepcopy(img)
        h, w = len(img), len(img[0])
        def smoother(x, y):
            node = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], \
                    [x - 1, y], [x, y], [x + 1, y], \
                    [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
            temp, result = 0, 0
            for a, b in node:
                if 0 <= a < h and 0 <= b < w:
                    result += ximg[a][b]
                    temp += 1
            return int(result / temp)
        
        for i in range(h):
            for j in range(w):
                img[i][j] = smoother(i, j)
        return img
