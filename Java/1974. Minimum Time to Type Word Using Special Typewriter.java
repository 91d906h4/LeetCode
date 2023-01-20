class Solution {
    public int minTimeToType(String word) {
        int ans = -1, t;
        word = "a" + word;
        char temp[] = word.toCharArray();

        for(int i = 0; i < temp.length - 1; i++){
            t = Math.abs(temp[i] - temp[i + 1]);
            ans += Math.min(t, 26 - t);
        }

        return ans + temp.length;
    }
}
