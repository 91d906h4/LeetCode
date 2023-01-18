class Solution {
    public int minSteps(String s, String t) {
        int x[] = new int[26], y[] = new int[26], ans = 0;
        
        for(char i: s.toCharArray()) x[(int)i - 97] += 1;
        for(char j: t.toCharArray()) y[(int)j - 97] += 1;

        for(int i = 0; i < 26; i++) ans += Math.abs(x[i] - y[i]);

        return ans / 2;
    }
}
