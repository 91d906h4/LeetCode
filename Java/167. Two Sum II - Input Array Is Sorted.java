class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int a = numbers.length - 1, b = 0;
        while(numbers[a] + numbers[b] != target){
            if(numbers[a] + numbers[b] > target){ a--; }
            else{ b++; }
        }
        int[] result = {b + 1, a + 1};
        return result;
    }
}
