/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    var a = n.toString(2);
    var b = 0, c = 1, d = 0;
    for(var i = 0;i < a.length;i++){
        if(a[i] == 0){
            c++;
        }
        else{
            if(b == 0){
                b++;
            }
            else{
                if(c > d) d = c;
                c = 1;
            }
        }
    }
    return d;
};
