/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
    var a = [];
    s.split("").forEach(element => {
        if(!a[element]) a[element] = "";
        a[element] += element;
    });
    var b = [], i = 0;
    for(let key in a){
        b[i] = a[key].length;
        i++;
    }
    for(var i = 0;i < b.length;i++){
        if(b[0] != b[i]) return false;
    }
    return true;
};
