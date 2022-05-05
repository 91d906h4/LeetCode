/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    var a = 0;
    accounts.forEach(element => {
        var b = 0;
        element.forEach(val => {
            b = b + val;
        });
        if(b > a) a = b;
    });
    return a;
};
