class Solution {
    public int characterReplacement(String s, int k) {
        int m = 0, r = 0;
        int[] t = new int[26];
        for(int i = 0; i < s.length(); i++){
            t[s.charAt(i) - 'A'] += 1;
            m = Math.max(m, t[s.charAt(i) - 'A']);
            if(r - m < k) r += 1;
            else t[s.charAt(i - r) - 'A'] -= 1;
        }
        return r;
    }
}
