class Solution {
    private int counter(int t[]){
        int res = 0;
        for(int i: t) res += i == 0 ? 0 : 1;
        return res;
    }

    public int numSplits(String s) {
        int l[] = new int[26], r[] = new int[26], ans = 0, temp;

        for(char i: s.toCharArray()) r[(int)i - 97]++;

        for(char i: s.toCharArray()){
            temp = (int)i - 97;
            if(counter(l) == counter(r)) ans++;
            l[temp]++;
            r[temp]--;
        }

        return ans;
    }
}
