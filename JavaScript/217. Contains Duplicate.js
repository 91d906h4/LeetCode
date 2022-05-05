/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var a = [];
    for(var i = 0;i < nums.length;i++){
        if(a.includes(nums[i])) return true;
        a.push(nums[i]);
    }
    return false;
};
