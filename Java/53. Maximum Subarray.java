class Solution {
    public int maxSubArray(int[] nums) {
        int t = nums[0], m = nums[0];

        for(int i = 1; i < nums.length; i++){
            t = Math.max(nums[i], t + nums[i]);
            m = Math.max(t, m);
        }

        return m;
    }
}
