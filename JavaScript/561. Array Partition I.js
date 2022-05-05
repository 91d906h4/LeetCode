/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort((a, b) => {return a - b;});
    var a = 0;
    for(var i = 0;i <nums.length;i+=2){
        a += nums[i];
    }
    return a;
};
