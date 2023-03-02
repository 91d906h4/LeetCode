class Solution {
public:
    int minPartitions(string n) {
        int m = 48;

        for(char& i: n){
            if((int)i > m) m = (int)i;
        }

        return m - 48;
    }
};
