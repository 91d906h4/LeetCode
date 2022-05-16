/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    var temp = 0;
    for(var i = 0; i < words.length;i++){
        if(words[i].startsWith(pref)){ temp++; }
    }
    return temp;
};
