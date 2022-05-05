/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    var a = [], b = 0;
    a[0] = first;
    encoded.forEach(element => {
        a.push(a[b] ^ element);
        b++;
    });
    return a;
};
