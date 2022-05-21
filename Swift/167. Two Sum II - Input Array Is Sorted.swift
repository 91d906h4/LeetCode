class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var a = numbers.count - 1, b = 0;
        while(numbers[a] + numbers[b] != target){
            if(numbers[a] + numbers[b] > target){ a -= 1; }
            else{ b += 1; }
        }
        return [b + 1, a + 1];
    }
}
