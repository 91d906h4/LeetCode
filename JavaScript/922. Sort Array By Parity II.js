/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
    var a = nums.filter(element => element % 2 == 0);
    var b = nums.filter(element => element % 2 == 1);
    var c = [];
    for(var i = 0;i < nums.length/2;i++){
        c.push(a[i]);
        c.push(b[i]);
    }
    return c;
};
