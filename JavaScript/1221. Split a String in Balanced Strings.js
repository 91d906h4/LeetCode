/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    var a = 0, b = 0;
    s.split("").forEach(element => {
        if(element == "R") a++;
        else a--;
        if(a == 0) b++;
    });
    return b;
};
