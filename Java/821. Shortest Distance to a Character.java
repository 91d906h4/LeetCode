class Solution {
    public int[] shortestToChar(String s, char c) {
        int l = s.length(), m;
        int temp[] = new int[l], res[] = new int[l];

        for(int i = 0; i < l; i++){
            if(s.charAt(i) == c) temp[i] = 1;
        }

        for(int i = 0; i < l; i++){
            m = 1001;
            for(int j = 0; j < l; j++){
                if(temp[j] == 1){
                    m = Math.min(m, Math.abs(j - i));
                }
            }
            res[i] = m;
        }

        return  res;
    }
}
