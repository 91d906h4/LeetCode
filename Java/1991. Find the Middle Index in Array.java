class Solution {
    public int findMiddleIndex(int[] nums) {
        int l = 0, r = 0, t;

        for(int i: nums) r += i;

        for(int i = 0; i < nums.length; i++){
            t = nums[i];
            if(l == r - t) return i;
            l += t;
            r -= t;
        }

        return -1;
    }
}
