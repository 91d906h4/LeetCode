/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    var a = jewels.split("");
    var b = stones.split("");
    var c = 0;
    a.forEach(elementa => {
        b.forEach(elementb => {
            if(elementa == elementb) c += 1;
        });
    });
    return c;
};
