/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    var a = numbers.length - 1, b = 0;
    while(numbers[a] + numbers[b] != target){
        if(numbers[a] + numbers[b] > target){ a--; }
        else{ b++; }
    }
    return [b + 1, a + 1];
};
