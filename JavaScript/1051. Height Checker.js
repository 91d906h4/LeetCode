/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    var a = [], b = 0;
    heights.forEach(element => {
        a.push(element);
    });
    heights.sort((a, b) => {return a - b;});
    for(var i = 0;i < heights.length;i++){
        if(heights[i] != a[i]) b++;
    }
    return b;
};
