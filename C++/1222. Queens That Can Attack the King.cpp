class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<int>> res;
        int x, y;

        for(int i = 0; i < 8; i++){
            if(i == 0) x = -1, y = -1;
            else if(i == 1) x = -1, y = 0;
            else if(i == 2) x = -1, y = 1;
            else if(i == 3) x = 0, y = -1;
            else if(i == 4) x = 0, y = 1;
            else if(i == 5) x = 1, y = -1;
            else if(i == 6) x = 1, y = 0;
            else if(i == 7) x = 1, y = 1;

            bool isAttacked = false, flag = false;
            int a = king[0], b = king[1];
            while(a >= 0 && b >= 0 && a < 8 && b < 8){
                flag = false;
                for(vector<int> temp: queens){
                    if(a == temp[0] && b == temp[1]){
                        res.push_back(temp);
                        flag = true;
                        break;
                    }
                }
                if(flag) break;
                a += x;
                b += y;
            }
        }

        return res;
    }
};
