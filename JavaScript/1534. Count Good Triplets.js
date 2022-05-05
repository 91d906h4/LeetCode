/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    var l = arr.length;
    var x = 0;
    for(let i = 0;i < l;i++){
        for(let j = i+1;j < l;j++){
            for(let k = j+1;k < l;k++){
                if(Math.abs(arr[i] - arr[j]) <= a &&
                   Math.abs(arr[j] - arr[k]) <= b &&
                   Math.abs(arr[i] - arr[k]) <= c){
                    x++;
                }
            }
        }
    }
    return x;
};
