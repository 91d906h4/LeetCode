/**
 * @param {number} num
 * @return {boolean}
 */
var isSameAfterReversals = function(num) {
    var a = String(num).split("");
    if(num == 0) return true;
    return (a[0] != 0 && a[a.length-1] != 0) ? true : false;
};
