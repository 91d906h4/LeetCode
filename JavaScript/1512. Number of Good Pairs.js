/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    var a = [];
    for(var i = 0;i <nums.length;i++){
        for(var j = i+1;j < nums.length;j++){
            if(nums[i] == nums[j]){
                var b = [i, j];
                a.push(b);
            }
        }
    }
    return a.length;
};
