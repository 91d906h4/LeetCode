/**
 * @param {string} word
 * @return {number}
 */
var numDifferentIntegers = function(word) {
    word = word.replace(/[a-z]/g, ".");
    var a = word.split(".");
    var b = [];
    var c = [];
    a.forEach(element => {
        if(element != "") b.push(BigInt(element));
    });
    b.forEach(element => {
        if(!c.includes(element)) c.push(element);
    });
    return c.length;
};
