/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    var a = [], b = "";
    a = s.split(" ");
    for(var i = 0;i < k;i++){
        b += a[i] + " ";
    }
    return b.substring(0, b.length - 1);
};
