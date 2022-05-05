/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    var a = [];
    var b = 0;
    for(var i = 1;i < n;i++){
        a.push(i);
        b += i;
    }
    a.push(b*-1);
    return a;
};
