class Solution {
    public int minFlips(String target) {
        int res = 0;
        char temp = '0';

        for(char i: target.toCharArray()){
            if(i != temp){
                res++;
                temp = i;
            }
        }

        return res;
    }
}
