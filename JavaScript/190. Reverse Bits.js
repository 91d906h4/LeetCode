/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    var a = n.toString(2).split("");
    while(a.length < 32){a.unshift('0');}
    return parseInt(a.reverse().join(""), 2);
};
