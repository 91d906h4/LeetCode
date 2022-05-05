/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    var a = num.toString().split("");
    a.sort();
    var x = a[0] + a[2];
    var y = a[1] + a[3];
    return parseInt(x) + parseInt(y);
};
