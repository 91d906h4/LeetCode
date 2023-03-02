class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;

        for(char i: jewels){
            for(char j: stones){
                if(i == j) res++;
            }
        }

        return res;
    }
};
