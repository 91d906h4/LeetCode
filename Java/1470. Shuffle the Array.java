class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] r = new int[n * 2];
        for(int i = 0; i < n * 2; i += 2){
            r[i] = nums[i / 2];
            r[i + 1] = nums[i / 2 + n];
        }
        return r;
    }
}
