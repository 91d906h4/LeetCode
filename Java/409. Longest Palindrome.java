class Solution {
    public int longestPalindrome(String s) {
        int[] map = new int[128];
        for(char c: s.toCharArray()){
            map[c]++;
        }
        int r = 0, t = 0;
        for(int v: map){
            if(v % 2 == 1){t = 1;}
            r += v / 2 * 2;
        }
        return r + t;
    }
}
