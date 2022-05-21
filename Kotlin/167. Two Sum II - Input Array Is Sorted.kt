class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var a = numbers.size - 1
        var b = 0
        while(numbers[a] + numbers[b] != target){
            if(numbers[a] + numbers[b] > target){ a-- }
            else{ b++ }
        }
        return intArrayOf(b + 1, a + 1)
    }
}
