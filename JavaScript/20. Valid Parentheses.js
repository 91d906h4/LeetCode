/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var a = [];
    var b = 0;
    s.split("").forEach(element => {
        if(element == "(" || element == "[" || element == "{") a.push(element);
        else if(element == ")"){
            if(a.pop() != "(") b=1;
        }
        else if(element == "]"){
            if(a.pop() != "[") b=1;
        }
        else if(element == "}"){
            if(a.pop() != "{") b=1;
        }
    });
    if(b != 0 || a.length != 0) return false;
    return true;
};
