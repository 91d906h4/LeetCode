/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    var a = 0;
    patterns.forEach(element => {
        if(word.includes(element)){
            a++;
        }
    });
    return a;
};
