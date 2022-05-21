impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut a = numbers.len() - 1;
        let mut b = 0;
        while numbers[a] + numbers[b] != target {
            if numbers[a] + numbers[b] > target { a -= 1; }
            else{ b += 1; }
        }
        return vec![(b + 1) as i32, (a + 1) as i32];
    }
}
