/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    var a = 0;
    nums.forEach(element => {
        a += (element.toString().length % 2 == 0) ? 1 : 0;
    });
    return a;
};
