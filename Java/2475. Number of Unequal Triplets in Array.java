class Solution {
    public int unequalTriplets(int[] nums) {
        int ans = 0, l = nums.length;

        for(int i = 0; i < l; i++){
            for(int j = i + 1; j < l; j++){
                for(int k = j + 1; k < l; k++){
                    if(nums[i] != nums[j] && nums[j] != nums[k] && nums[i] != nums[k]){
                        ans++;
                    }
                }
            }
        }

        return ans;
    }
}
