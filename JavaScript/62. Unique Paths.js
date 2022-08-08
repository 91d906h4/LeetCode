/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    var factorial = (k) => {
        let r = 1;
        for(let i = 1; i <= k; i++) r *= i;
        return r;
    }
    return factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1));
};
