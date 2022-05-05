/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    var a = new Array(nums.length);
    a.fill(0);
    for(var i = 0;i < nums.length;i++){
        for(var j = 0;j <= i;j++){
            a[i] = a[i] + nums[j];
        }
    }
    return a;
};
