/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    var a = [], b = [];
    for(var i = 0;i < s.length;i++){
        if(!s[i].match(/[a-zA-Z]/)) b[i] = String(s[i].match(/[^a-zA-Z]/));
    }
    a = s.replace(/[^a-zA-Z]/g, "").toString().split("").reverse();
    for(var i = 0;i < s.length;i++){
        if(b[i]) a.splice(i, 0, b[i]);
    }
    return a.join("");
};
