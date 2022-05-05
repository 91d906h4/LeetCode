/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    var a = s.split(" ");
    var c = "";
    a.forEach(element => {
        var b = element.split("").reverse();
        c += b.join("") + " ";
    });
    return c.substring(0, c.length-1);
};
