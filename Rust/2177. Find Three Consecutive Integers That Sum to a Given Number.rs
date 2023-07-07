impl Solution {
    pub fn sum_of_three(num: i64) -> Vec<i64> {
        let a = num / 3;
        let b = num % 3;

        if b == 0 {
            return vec![a - 1, a, a + 1];
        }
        return vec![];
    }
}
