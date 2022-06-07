/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    return JSON.stringify(target.sort()) === JSON.stringify(arr.sort());
};
