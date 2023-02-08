class Solution {
    public int maxProfit(int[] prices) {
        int t = prices[0], res = 0;

        for(int i: prices){
            if(i > t) res += i - t;
            t = i;
        }

        return res;
    }
}
