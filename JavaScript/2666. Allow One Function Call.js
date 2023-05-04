/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var t = 0;
    return function(...args){
        return t++ == 0 ? fn(...args) : undefined;
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
