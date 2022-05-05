/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
//     if(s.length != t.length) return false;
//     var a = {};
//     for(var i = 0;i < s.length;i++){
//         if(!a[s[i]]) a[s[i]] = t[i];
//         else if(a[s[i]] != t[i]) return false;
//     }
//     var a = {};
//     for(var i = 0;i < t.length;i++){
//         if(!a[t[i]]) a[t[i]] = s[i];
//         else if(a[t[i]] != s[i]) return false;
//     }
//     return true;

    if(s.length != t.length) return false;
    var a = {}, b = {};
    for(var i = 0;i < s.length;i++){
        if(a[s[i]] != b[t[i]]) return false;
        else{
            a[s[i]] = i;
            b[t[i]] = i;
        }
    }
};
