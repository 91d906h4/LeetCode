class Solution {
    public int pivotInteger(int n) {
        int x = 1, y = n * (n + 1) / 2;

        for(int i = 1; i <= n; i++){
            if(x > y) return -1;
            if(x == y) return i;
            x += i + 1;
            y -= i;
        }

        return -1;
    }
}
