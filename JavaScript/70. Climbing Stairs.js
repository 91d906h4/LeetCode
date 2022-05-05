/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // Recursion
    // if(n == 0 || n == 1 || n == 2) return n;
    // else{
    //     return climbStairs(n-1) + climbStairs(n-2);
    // }
    var a = [];
    a[0] = 0; a[1] = 1; a[2] = 2;
    for(var i = 3;i <= n;i++){
        a[i] = a[i-1] + a[i-2];
    }
    return a[n];
};
