func twoSum(numbers []int, target int) []int {
    a, b := len(numbers) - 1, 0
    for true{
        if numbers[a] + numbers[b] > target {
            a--
        } else if numbers[a] + numbers[b] < target {
            b++
        } else {
            return []int{b + 1, a + 1}
        }
    }
    return []int{b + 1, a + 1}
}
