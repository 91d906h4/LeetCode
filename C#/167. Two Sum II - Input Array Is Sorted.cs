public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var a = numbers.Length - 1;
        var b = 0;
        while(numbers[a] + numbers[b] != target){
            if(numbers[a] + numbers[b] > target){ a--; }
            else{ b++; }
        }
        int[] result = {b + 1, a + 1};
        return result;
    }
}
