/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    strs.sort((a, b) => {return a.length - b.length;});
    var a = strs[0];
    for(var i = 0;i < strs.length-1;i++){
        for(var j = 0;j < strs[0].length;j++){
            if(strs[i][j] != strs[i+1][j]) a = a.substring(0, j);
        }
    }
    return a;
};
