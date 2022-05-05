/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    var a = [];
    for(var i = left;i <= right;i++){
        var b = String(i).split("");
        var len = b.length;
        for(var j = 0;j < len;j++){
            if(i % b[j] != 0) break;
        }
        if(j == len) a.push(i);
    }
    return a;
};
