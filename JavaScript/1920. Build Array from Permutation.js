/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    var a = [];
    for(var i = 0;i < nums.length;i++){
        a[i] = nums[nums[i]];
    }
    return a;
};
