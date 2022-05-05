/**
 * @param {string} s
 * @return {string[]}
 */
var cellsInRange = function(s) {
    var x = s[0].charCodeAt(0), y = s[3].charCodeAt(0);
    var x_t = s[1], y_t = s[4];
    var a = [];
    if(x_t >= y_t){
        t = x_t;
        ut = y_t;
    }
    else{
        ut = x_t;
        t = y_t;
    }
    for(var i = x;i <= y;i++){
        for(var j = ut;j <= t;j++){
            a.push((String.fromCharCode(i) + j));
        }
    }
    return a;
};
