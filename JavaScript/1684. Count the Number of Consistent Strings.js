/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    var a = allowed.split("");
    var b = 0;
    words.forEach(elementa => {
        a.forEach(elementb => {
            elementa = elementa.replaceAll(elementb, "");
        });
        if(elementa.length == 0) b++;
    });
    return b;
};
