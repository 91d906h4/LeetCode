class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int a = numbers.size() - 1, b = 0;
        while(numbers[a] + numbers[b] != target){
            if(numbers[a] + numbers[b] > target){ a--; }
            else{ b++; }
        }
        vector<int> result{b + 1, a + 1};
        return result;
    }
};
