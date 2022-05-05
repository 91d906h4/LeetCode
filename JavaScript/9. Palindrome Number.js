/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var a = x.toString();
    var b = a.split("").reverse();
    var c = "";
    b.forEach(element => {
        c += element;
    });
    return a == c ? true : false;
};
