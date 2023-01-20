class Solution {
    private int checkRepeat(String t){
        int temp[] = new int[26];

        for(char i: t.toCharArray()){
            if(temp[(int)i - 97] != 0) return 1;
            temp[(int)i - 97] = 1;
        }

        return -1;
    }

    public int countGoodSubstrings(String s) {
        if(s.length() == 1) return 0;

        int res = 0;
        String t = "0" + s.substring(0, 2);

        for(char i: s.substring(2, s.length()).toCharArray()){
            t = t.substring(1, 3) + String.valueOf(i);
            if(checkRepeat(t) == -1) res++;
        }

        return res;
    }
}
