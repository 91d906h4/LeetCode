/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var a = [], b = nums.length;
    var t = 0;
    for(var i = 0;i < b;i+=2){
        a[i] = nums[t];
        a[i+1] = nums[t+n];
        t++;
    }
    return a;
};
