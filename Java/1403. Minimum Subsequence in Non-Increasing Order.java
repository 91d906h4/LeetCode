import java.util.Arrays;
import java.util.Collections;

class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        int s = 0;
        ArrayList<Integer> ans = new ArrayList<>();

        Arrays.sort(nums);

        for(int i: nums) s += i;
        for(int i = nums.length - 1; i >= 0; i--){
            s -= nums[i] * 2;
            ans.add(nums[i]);
            if(s < 0) break;
        }

        return ans;
    }
}
