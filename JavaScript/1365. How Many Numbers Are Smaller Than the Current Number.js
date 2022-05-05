/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    var b = [];
    nums.forEach(elementa => {
        var a = 0;
        nums.forEach(elementb => {
            if(elementa > elementb) a++;
        });
        b.push(a);
    });
    return b;
};
