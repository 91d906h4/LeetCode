/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
//     nums.push(target);
//     nums = nums.sort((a, b) => a - b);
//     for(var i = 0;i < nums.length;i++){
//         if(nums[i] == target) return i;
//     }

    var high = nums.length - 1;
    var low = 0;
    while(high >= low){
        var mid = ~~((high + low) / 2);
        if(nums[mid] == target){ return mid; }
        else if(nums[mid] > target){ high = mid - 1; }
        else if(nums[mid] < target){ low = mid + 1; }
    }
    return low;
};
