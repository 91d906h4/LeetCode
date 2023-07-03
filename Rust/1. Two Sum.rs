use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut temp: HashMap<i32, usize> = HashMap::new();

        for (i, j) in nums.iter().enumerate() {
            if temp.contains_key(j) {
                return vec![temp.get(j).unwrap().clone() as i32, i as i32];
            }
            else {
                temp.insert(target - j, i);
            }
        }

        return vec![0, 0];
    }
}
