/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var a = 0, b = 0;
    for(var i = 0;i < nums.length;i++){
        if(b == 0){
            a = nums[i];
            b++;
        }
        else{
            if(a == nums[i]) b++;
            else b--;
        }
    }
    return a;
};
