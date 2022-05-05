/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    var a = 0, b = 0;
    for(var i = 0;i < gain.length;i++){
        b += gain[i];
        if(b > a) a = b;
    }
    return a;
};
