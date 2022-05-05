/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    var a = [];
    nums.sort((a, b) => {return a - b;});
    for(var i = 0;i < nums.length;i++){
        if(nums[i] == target) a.push(i);
    }
    return a;
};
