/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    function result(string){
        var a = [];
        for(var i = 0;i < string.length;i++){
            if(string[i] == "#") a.pop();
            else a.push(string[i]);
        }
        return a.join("");
    }
    return result(s) == result(t);
};
