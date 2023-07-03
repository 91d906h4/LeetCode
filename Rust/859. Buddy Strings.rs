use std::collections::HashMap;

impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        if s.len() != goal.len() { return false; }

        let mut temp: Vec<usize> = Vec::new();

        for (i, j) in s.chars().enumerate() {
            if let Some(t) = goal.chars().nth(i) {
                if j != t {
                    temp.push(i);
                }
            }
        }

        if temp.len() > 2 {
            return false;
        }
        else if temp.len() == 2 {
            return goal.chars().nth(temp[0]) == s.chars().nth(temp[1]) &&
                   goal.chars().nth(temp[1]) == s.chars().nth(temp[0]);
        }
        else {
            if s == goal {
                let mut temp: HashMap<char, i32> = HashMap::new();

                for i in s.chars() {
                    if temp.contains_key(&i) {
                        *temp.get_mut(&i).unwrap() += 1;
                    }
                    else {
                        temp.insert(i, 1);
                    }
                }

                for i in temp.values() {
                    if i >= &2 {
                        return true;
                    }
                }

                return false;
            }
            else {return false;}
        }
    }
}
