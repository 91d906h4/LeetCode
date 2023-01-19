class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashMap<Integer, Integer> temp = new HashMap<>();
        List<Integer> ans = new ArrayList<>();

        for(int i: nums){
            if(temp.get(i) != null) ans.add(i);
            else temp.put(i, 1);
        }

        return ans;
    }
}
