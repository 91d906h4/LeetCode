/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var a = String(x).split("");
    var b = "";
    if(a[0] == "-"){
        a.shift();
        b = "-";
    }
    var c = BigInt(b + a.reverse().join(""));
    return (c > -1 * Math.pow(2, 31) && c < Math.pow(2, 31) - 1) ? c : 0;
};
