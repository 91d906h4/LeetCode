/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
//     for(var i = 0;i < nums.length;i++){
//         for(var j = i+1;j < nums.length;j++){
//             if(nums[i] + nums[j] == target) return [i, j];
//         }
//     }

    var a = 0;
    for(var i = 0;i < nums.length;i++){
        a = target - nums[i];
        if(nums.includes(a) && nums.indexOf(a) != i) return [i, nums.indexOf(a)];
    }
};
