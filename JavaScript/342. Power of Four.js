/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if(n == 1) return true;
    if(n % 2 == 1) return false;
    var a = Infinity;
    for(var i = 1;i<= n;i*=4){if(i == n) return true;}
    return false;
};
