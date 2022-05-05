/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    var a = 0, b;
    sentences.forEach(element => {
        b = element.split(" ");
        if(b.length > a) a = b.length;
    });
    return a;
};
