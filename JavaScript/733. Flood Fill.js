/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    var o = image[sr][sc], ir = image.length, ic = image[0].length;
    if(o == newColor) return image;
    function dfs(r, c){
        if(image[r][c] == o){
            image[r][c] = newColor;
            if(r > 0) dfs(r - 1, c);
            if(r + 1 < ir) dfs(r + 1, c);
            if(c > 0) dfs(r, c - 1);
            if(c + 1 < ic) dfs(r, c + 1);
        }
    }
    dfs(sr, sc);
    return image;
};
