/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    var a = [], b = 0;
    index.forEach(element => {
        a.splice(element, 0, nums[b]);
        b++;
    });
    return a;
};
