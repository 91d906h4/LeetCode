/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    var a = 0;
    var str = n.toString(2);
    for(var i = 0;i < str.length;i++){
        if(str[i] == 1) a++;
    }
    return a;
};
