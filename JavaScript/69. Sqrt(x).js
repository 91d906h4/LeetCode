/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
//     for(var i = 1;i <= 65536;i++){
//         if(i * i == x) return i;
//         if(i * i > x) return i - 1;
//     }

    let low = 1;
    let high = Math.round(x / 2);
    let result = 0;
    while(low <= high){
        let temp = low + Math.round((high - low) / 2);
        let pow = temp * temp;
        if(pow == x){
            result = temp;
            break;
        }
        else if(pow > x){
            high = temp - 1;
        }
        else{
            low = temp + 1;
            result = temp;
        }
    }
    return result;
};
