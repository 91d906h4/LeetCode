/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    var a = [], b = 0;
    for(var i = 0;i < nums1.length;i++){
        b = nums1[i];
        for(var j = nums2.indexOf(b);j < nums2.length;j++){
            if(nums2[j] > b){
                a.push(nums2[j]);
                break;
            }
        }
        if(j == nums2.length) a.push(-1);
    }
    return a;
};
