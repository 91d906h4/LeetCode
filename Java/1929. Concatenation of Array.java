class Solution {
    public int[] getConcatenation(int[] nums) {
        int l = nums.length;
        int[] ans = new int[l * 2];

        for(int i = 0; i < 2; i++){
            for(int j = 0; j < l; j++){
                ans[i * l + j] = nums[j];
            }
        }

        return ans;
    }
}
