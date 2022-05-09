/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var sumBase = function(n, k) {
    var a = n.toString(k).split("");
    var result = 0;
    for(var i = 0;i < a.length;i++){
        result += parseInt(a[i]);
    }
    return result;
};
