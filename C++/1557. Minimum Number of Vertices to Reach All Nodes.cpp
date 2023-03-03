class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        map<int, int> counter;
        vector<int> res;

        for(vector<int> i: edges){
            if(!counter.count(i[0])) counter[i[0]] = 0;
            
            if(counter.count(i[1])) counter[i[1]]++;
            else counter[i[1]] = 1;
        }

        for(auto &[k, v]: counter){
            if(v == 0) res.push_back(k);
        }

        return res;
    }
};
