/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var a = nums[0], b = nums[0];
    for(var i = 1;i < nums.length;i++){
        if(a + nums[i] < nums[i]) a = nums[i];
        else a += nums[i];
        b = (a > b) ? a : b;
    }
    return b;
};
