/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    var a = [];
    for(var i = 0;i < matrix[0].length;i++){
        var b = [];
        for(var j = 0;j < matrix.length;j++){
            b.push(matrix[j][i]);
        }
        a.push(b);
    }
    return a;
};
