class Solution {
    public int minMoves(int[] nums) {
        int ans = 0, m = Integer.MAX_VALUE;

        for(int i: nums) if(i < m) m = i;
        for(int i: nums) ans += i - m;

        return ans;
    }
}
