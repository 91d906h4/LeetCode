/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    // return n.split("").sort((a, b) => {return b - a;})[0];
    
    for(var i = 9;i >= 0;i--){
        if(n.indexOf(i) != -1) return i;
    }
};
