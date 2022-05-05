/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
    var a = start;
    for(var i = 1;i < n;i++){
        a = a ^ (start + 2);
        start += 2;
    }
    return a;
};
