/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    var a = [];
    if(n == 1) return true;
    while(!a.includes(n)){
        a.push(n);
        n = String(n).split("");
        n = n.reduce((a, b) => 
            a + b * b
        , 0);
        if(n == 1){
            return true;
        }
    }
    return false;
};
