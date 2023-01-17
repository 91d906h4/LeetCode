class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int ans = 0;

        for(char i: stones.toCharArray()){
            if(jewels.indexOf(i) != -1) ans++;
        }

        return ans;
    }
}
