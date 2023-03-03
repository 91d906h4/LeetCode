class Solution {
public:
    string getHappyString(int n, int k) {
        vector<string> happy = {"a", "b", "c"}, temp;
        
        for(int i = 1; i < n; i++){
            for(int j = 0; j < happy.size(); j++){
                for(char c: {'a', 'b', 'c'}){
                    if(happy[j].back() != c) temp.push_back(happy[j] + c);
                }
            }
            happy = temp;
            temp = {};
        }

        sort(happy.begin(), happy.end());

        return happy.size() >= k ? happy[k - 1] : "";
    }
};
