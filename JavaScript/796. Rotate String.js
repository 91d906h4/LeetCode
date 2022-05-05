/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
//     var b = s.toString();
//     for(var i = 0;i < s.length;i++){
//         var a = b.toString().split(""); 
//         a.push(a[0]);
//         a.shift();
//         a = a.join("");
//         if(a == goal) return true;
//         b = a;
//     }
//     return false;

    for(var i = 0;i < s.length;i++){
        if(s.substring(i, s.length) + s.substring(0, i) == goal) return true;
    }
    return false;
};
