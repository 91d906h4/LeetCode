/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function(start, goal) {
    var a = start.toString(2).split("");
    var b = goal.toString(2).split("");
    var c = 0;
    while(a.length != b.length){
        if(a.length > b.length) b.unshift("0");
        else if(a.length < b.length) a.unshift("0");
    }
    console.log(a, b);
    for(var i = 0;i < a.length;i++){
        c += (a[i] != b[i]) ? 1 : 0;
    }
    return c;
};
