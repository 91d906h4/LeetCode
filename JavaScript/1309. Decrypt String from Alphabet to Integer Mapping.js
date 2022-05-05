/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
//     var a = "";
//     while(s.length > 0){
//         if(s[2] == "#"){
//             a += String.fromCharCode(Number(s.substring(0, 2)) + 96);
//             s = s.substring(3, s.length);
//         }
//         else{
//             a += String.fromCharCode(Number(s.substring(0, 1)) + 96);
//             s = s.substring(1, s.length);
//         }
//     }
//     return a;

    var a = "";
    while(s.length > 0){
        a += String.fromCharCode(Number(s.substring(0, ((s[2] == "#") ? 2 : 1))) + 96);
        s = s.substring(((s[2] == "#") ? 3 : 1), s.length);
    }
    return a;
};
