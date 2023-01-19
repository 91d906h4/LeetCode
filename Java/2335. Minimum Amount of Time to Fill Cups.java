class Solution {
    public int fillCups(int[] amount) {
        int m, res = 0, c = amount[0], w = amount[1], h = amount[2];

        while(c > 0 || w > 0 || h > 0){
            m = Math.min(Math.min(c, w), h);

            if(m == c){
                w--;
                h--;
            }
            else if(m == w){
                c--;
                h--;
            }
            else if(m == h){
                c--;
                w--;
            }

            res++;
        }

        return res;
    }
}
