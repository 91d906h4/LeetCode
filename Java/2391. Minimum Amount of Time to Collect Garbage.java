class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int m = 0, p = 0, g = 0, l = 0;
        String temp;

        for(int i = 0; i < garbage.length; i++){
            temp = garbage[i];
            if(temp.indexOf("M") != -1) m = i;
            if(temp.indexOf("P") != -1) p = i;
            if(temp.indexOf("G") != -1) g = i;
            l += temp.length();
        }

        int res = 0, t = 0;
        for(int i = 0; i < travel.length; i++){
            t = travel[i];
            if(m > 0){
                res += t;
                m--;
            }
            if(p > 0){
                res += t;
                p--;
            }
            if(g > 0){
                res += t;
                g--;
            }
        }

        return res + l;
    }
}
