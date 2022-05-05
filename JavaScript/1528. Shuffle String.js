/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    var a = [], b = 0;
    for(var i = 0;i < s.length;i++){
        a[indices[i]] = s[i];
    }
    return a.join("");
};
