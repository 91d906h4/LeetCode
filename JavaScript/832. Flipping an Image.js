/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    var a = [];
    for(var i = 0;i <image.length;i++){
        var b = [];
        for(var j = 0;j < image[i].length;j++){
            b.push(image[i][j] ^ 1);
        }
        b.reverse();
        a.push(b);
    }
    return a;
};
