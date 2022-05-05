/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    return s.split(" ").reverse().find(element => element != "").length;
};
