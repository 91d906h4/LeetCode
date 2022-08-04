class Solution {
    public int maxDistance(int[] colors) {
        int l = colors.length - 1;
        int i = 0, j = l;
        while(colors[i] == colors[l] && colors[0] == colors[j]){
            i += 1;
            j -= 1;
        }
        return Math.max(l - i, j - 0);
    }
}
