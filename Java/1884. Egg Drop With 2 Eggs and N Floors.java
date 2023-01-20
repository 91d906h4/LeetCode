class Solution {
    public int twoEggDrop(int n) {
        int t = n;

        for(int i = 1; i <= t + 1; i++){
            n -= i;
            if(n <= 0) return i;
        }
        return 0;
    }
}
