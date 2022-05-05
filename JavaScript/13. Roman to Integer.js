/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var a = s.toString().split("");
    var x = 0;
    var table = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ];
    while(a.length > 0){
        for(var i = 12;i => 0;i--){
            if(a[0] + a[1] == table[i][0]){x += table[i][1]; a.shift(); a.shift(); break;}
            else if(a[0] == table[i][0]){x += table[i][1]; a.shift(); break;}
        }
    }
    return x;
};
