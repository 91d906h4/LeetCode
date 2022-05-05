/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    var a = 0;
    var b = [];
    a = Math.max(...candies);
    candies.forEach(element => {
        b.push((element + extraCandies >= a) ? true : false);
    });
    return b;
};
