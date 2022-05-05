/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    return nums.filter(element => element % 2 == 0).concat(nums.filter(element => element % 2 == 1));
};
