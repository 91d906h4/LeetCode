/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    var l = nums.length;
    var a = 0;
    for(var i = 0;i < l;i++){
        for(var j = i+1;j < l;j++){
            if(nums[i] == nums[j]){
                a += ((i * j) % k == 0) ? 1 : 0;
            }
        }
    }
    return a;
};
