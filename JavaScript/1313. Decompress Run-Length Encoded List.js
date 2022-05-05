/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    var a = [];
    for(var i = 0;i < nums.length;i+=2){
        for(var j = 0;j < nums[i];j++){
            a.push(nums[i+1]);
        }
    }
    return a;
};
