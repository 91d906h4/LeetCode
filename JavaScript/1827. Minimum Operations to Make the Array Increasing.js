/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
//     var a = 0;
//     for(var i = 1;i < nums.length;i++){
//         while(nums[i] <= nums[i-1]){
//             nums[i]++;
//             a++;
//         }
//     }
//     return a;

    var a = 0, b = 0;
    for(var i = 0;i < nums.length;i++){
        if(nums[i] > a){
            a = nums[i];
        }
        else{
            b += ++a - nums[i];
        }
    }
    return b;
};
