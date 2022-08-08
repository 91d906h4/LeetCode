/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    var m = 0, r = 0, t = {};
    for(var i = 0; i < s.length; i++){
        if(!t[s[i]]) t[s[i]] = 1;
        else t[s[i]] += 1;
        m = Math.max(m, t[s[i]]);
        if(r - m < k) r += 1;
        else t[s[i - r]] -= 1;
    }
    return r;
};
