class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(hashmap.containsKey(nums[i])){
                int t = hashmap.get(nums[i]);
                return new int[]{t, i};
            }
            else{
                hashmap.put(target - nums[i], i);
            }
        }
        return new int[2];
    }
}
