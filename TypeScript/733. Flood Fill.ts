function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    var o: number = image[sr][sc], ir: number = image.length, ic: number = image[0].length;
    if(o == color) return image;
    const dfs = (r, c) => {
        if(image[r][c] == o){
            image[r][c] = color;
            if(r > 0) dfs(r - 1, c);
            if(r + 1 < ir) dfs(r + 1, c);
            if(c > 0) dfs(r, c - 1);
            if(c + 1 < ic) dfs(r, c + 1);
        }
    }
    dfs(sr, sc);
    return image;
};
