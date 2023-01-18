class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int x[] = new int[m], y[] = new int[n], ans = 0;

        for(int[] i: indices){
            x[i[0]] += 1;
            y[i[1]] += 1;
        }

        for(int i: x){
            for(int j: y){
                if((i + j) % 2 == 1) ans++;
            }
        }

        return ans;
    }
}
