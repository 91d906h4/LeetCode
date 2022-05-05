/**
 * @param {number[]} aliceSizes
 * @param {number[]} bobSizes
 * @return {number[]}
 */
var fairCandySwap = function(aliceSizes, bobSizes) {
    var a = aliceSizes.reduce((a, b) => a + b);
    var b = bobSizes.reduce((a, b) => a + b);
    for(var i = 0;i < aliceSizes.length;i++){
        for(var j = 0;j < bobSizes.length;j++){
            if(a - aliceSizes[i] * 2 == b - bobSizes[j] * 2){
                return [aliceSizes[i], bobSizes[j]];
            }
        }
    }
};
