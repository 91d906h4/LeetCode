/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    var a = 0, b = 0;
    s.split("").forEach(element => {
        if(element == "(") a++;
        else if(element == ")") a--;
        b = (a > b) ? a : b;
    });
    return b;
};
