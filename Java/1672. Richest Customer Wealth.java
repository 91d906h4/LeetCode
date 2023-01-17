class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0, temp = 0;

        for(int[] i: accounts){
            temp = 0;
            for(int j: i) temp += j;
            ans = Math.max(ans, temp);
        }

        return ans;
    }
}
