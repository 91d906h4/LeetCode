/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
//     var a = String(num).split("");
//     for(var i = 0;i < a.length;i++){
//         if(a[i] == 6){
//             a[i] = 9;
//             break;
//         }
//     }
//     return a.join("");

    return Number(String(num).replace("6", "9"));
};
