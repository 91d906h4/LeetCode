/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var a = [];
    for(var i = 0;i < nums.length;i++){
        if(a.includes(nums[i])) nums[i] = "101";
        else a.push(nums[i]);
    }
    nums.sort((a, b) => {
        return a - b;
    });
    return a.length;
};
