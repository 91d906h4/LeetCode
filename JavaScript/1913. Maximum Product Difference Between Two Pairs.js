/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    var a = Math.max(...nums);
    nums.splice(nums.indexOf(a), 1);
    var b = Math.max(...nums);
    nums.splice(nums.indexOf(b), 1);
    var c = Math.min(...nums);
    nums.splice(nums.indexOf(c), 1);
    var d = Math.min(...nums);
    nums.splice(nums.indexOf(d), 1);
    return (a * b) - (c * d);
};
