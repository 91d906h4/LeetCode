/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    var a = "";
    for(var i = 0;i < words.length;i++){
        if(words[i].split("").join("") == words[i].split("").reverse().join("")){
            a = words[i];
            break;
        }
    }
    return a;
};
