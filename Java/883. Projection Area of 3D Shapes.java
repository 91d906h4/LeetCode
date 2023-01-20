class Solution {
    private int max(int[] array){
        int m = 0;
        for(int i: array) m = Math.max(m, i);
        return m;
    }

    public int projectionArea(int[][] grid) {
        int res = 0, temp = 0, m;
        
        for(int[] x: grid) res += max(x);
        for(int i = 0; i < grid.length; i++){
            m = 0;
            for(int j = 0; j < grid[0].length; j++){
                m = Math.max(m, grid[j][i]);
                if(grid[j][i] != 0) temp++;
            }
            res += m;
        }

        return res + temp;
    }
}
