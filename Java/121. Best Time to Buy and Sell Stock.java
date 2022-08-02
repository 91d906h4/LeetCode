class Solution {
    public int maxProfit(int[] prices) {
        int m = prices[0], r = 0;
        for(int i: prices){
            if(i < m){m = i;}
            if(i - m > r){r = i - m;}
        }
        return r;
    }
}
