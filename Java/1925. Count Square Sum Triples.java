class Solution {
    public int countTriples(int n) {
        int ans = 0;
        double temp;

        for(int i = 1; i < n; i++){
            for(int j = 1; j < n; j++){
                temp = Math.sqrt(i * i + j * j);
                if(temp <= n && temp == (int)temp) ans++;
            }
        }

        return ans;
    }
}
