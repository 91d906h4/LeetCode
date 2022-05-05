 /**
 * @param {string} s
 * @return {string}
 */
var replaceDigits = function(s) {
    var a = [];
    for(var i = 0;i < s.length;i+=2){
        a[i] = s[i];
        if(s[i+1]) a[i+1] = String.fromCharCode((parseInt(s[i].charCodeAt(0)) + parseInt(s[i+1])));
    }
    return a.join("");
};
