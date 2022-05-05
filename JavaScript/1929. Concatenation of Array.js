/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    var a = [];
    for(var i = nums.length - 1;i >= 0 ;i--) a.unshift(nums[i]);
    for(var i = nums.length - 1;i >= 0 ;i--) a.unshift(nums[i]);
    return a;
};
