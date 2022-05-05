/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    var a = 0;
    for(var i = 0;i < nums.length;i++){
        for(var j = i;j < nums.length;j++){
            if(nums[i] - nums[j] == k || nums[j] - nums[i] == k) a++;
        }
    }
    return a;
};
