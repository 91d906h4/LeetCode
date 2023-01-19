class Solution {
    public int minSteps(String s, String t) {
        int temp = 0, sc[] = new int[26], tc[] = new int[26];

        for(char i: s.toCharArray()) sc[(int)i - 97] += 1;
        for(char j: t.toCharArray()) tc[(int)j - 97] += 1;

        for(int k = 0; k < 26; k++){
            if(tc[k] != 0 && sc[k] != 0) temp += Math.min(sc[k], tc[k]) * 2;
        }

        return s.length() + t.length() - temp;
    }
}
