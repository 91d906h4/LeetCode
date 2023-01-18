import java.util.Arrays;

class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);

        int res = 0;
        for(int i: costs){
            if(coins - i >= 0){
                coins -= i;
                res += 1;
            }
            else break;
        }

        return res;
    }
}
