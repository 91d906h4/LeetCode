/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    var good_num = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"];
    for(var i = 0;i < 10;i++){
        if(num.indexOf(good_num[i]) != -1) return good_num[i];
    }
    return "";
};
