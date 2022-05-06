/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    var a = [], b = 0, c = 0;
    a = nums1.concat(nums2);
    a.sort((a, b) => {return a - b;});
    b = a.length % 2;
    c = ~~(a.length / 2);
    if(b){
        return a[c];
    }
    else{
        return (a[c-1] + a[c])/2
    }
};
