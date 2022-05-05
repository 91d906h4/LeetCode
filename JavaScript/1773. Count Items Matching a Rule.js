/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    var a = 0, b = 0;
    switch(ruleKey){
        case "type":
            a = 0; break;
        case "color":
            a =1; break;
        default:
            a = 2; break;
    }

    items.forEach(element => {
        if(element[a] == ruleValue) b++;
    });
    return b;
};
