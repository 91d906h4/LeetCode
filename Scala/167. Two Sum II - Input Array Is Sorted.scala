object Solution {
    def twoSum(numbers: Array[Int], target: Int): Array[Int] = {
        var a = numbers.size - 1
        var b = 0
        while(numbers(a) + numbers(b) != target){
            if(numbers(a) + numbers(b) > target){ a -= 1 }
            else{ b += 1 }
        }
        Array(b + 1, a + 1)
    }
}
