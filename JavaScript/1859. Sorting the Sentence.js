/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    var a = s.split(" ");
    var b = [], c = "";
    a.forEach(element => {
        var l = element.length-1;
        var x = element[l];
        b[x] = element.substring(0, l);
    });
    b.shift();
    return b.join(" ");
};
