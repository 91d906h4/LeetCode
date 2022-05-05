/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    var X = 0;
    operations.forEach(element => {
        if(element == "++X" || element == "X++") X += 1;
        else X -= 1;
    });
    return X;
};
