/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var a = 0;
    for(var i = 0;i < nums.length;i++){
        if(nums[i] == val){
            nums.splice(i, 1, "51");
        }
        else a++;
    }
    nums.sort((a, b) => a - b);
    return a;
};
