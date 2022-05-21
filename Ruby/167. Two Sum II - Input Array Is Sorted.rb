# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    a, b = numbers.size - 1, 0
    while numbers[a] + numbers[b] != target do
        if numbers[a] + numbers[b] > target then
            a -= 1
        else
            b += 1
        end
    end
    return [b + 1, a + 1]
end
