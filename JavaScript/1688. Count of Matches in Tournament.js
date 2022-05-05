/**
 * @param {number} n
 * @return {number}
 */
var numberOfMatches = function(n) {
    var a = 0;
    while(n > 1){
        if(n % 2){
            n = (n - 1) / 2;
            a += n;
            n += 1;
        }
        else{
            n /= 2;
            a += n;
        }
    }
    return a;
};
