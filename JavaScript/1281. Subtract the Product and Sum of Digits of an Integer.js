/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    var a = n.toString().split("");
    var b = 1, c = 0;
    a.forEach(element => {
        b = b* parseInt(element);
        c += parseInt(element);
    });
    return parseInt(b) - parseInt(c);
};
