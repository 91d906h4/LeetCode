/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    //nums.sort((a, b) => {return a - b;});
    var a = 0;
    for(var i = 0;i < nums.length-1;i++){
        if(!(nums[i] <= nums[i+1])){
            a += 1;
            break;
        }
    }
    for(var i = 0;i < nums.length-1;i++){
        if(!(nums[i] >= nums[i+1])){
            a += 1;
            break;
        }
    }
    if(a == 2) return false;
    else return true;
};
