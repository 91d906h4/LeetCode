/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    for(var i = 1;i <= 65536;i++){
        if(i * i == x) return i;
        if(i * i > x) return i - 1;
    }
};
