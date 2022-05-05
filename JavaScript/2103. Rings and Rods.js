/**
 * @param {string} rings
 * @return {number}
 */
var countPoints = function(rings) {
    var a = [];
    var b = 0;
    for(var i = 0;i < rings.length;i+=2){
        a[rings[(i+1)]] += rings[i];
    }
    a.forEach(element => {
        if(element.includes("R") && element.includes("G") && element.includes("B")) b++;
    });
    return b;
};
