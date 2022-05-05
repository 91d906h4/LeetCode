/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    var a = [];
    sentence.split("").forEach(element => {
        if(!a.includes(element)) a.push(element);
    });
    return a.length == 26;
};
