class Solution {
    public int numIdenticalPairs(int[] nums) {
        int temp[] = new int[101], ans = 0;

        for(int i: nums) temp[i]++;
        for(int i: temp) ans += i * (i - 1) / 2;

        return ans;
    }
}
