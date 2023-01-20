class Solution {
    public List<Integer> circularPermutation(int n, int start) {
        List<Integer> ans = new ArrayList<>();

        for(int i = 0; i < (1 << n); i++) ans.add(i ^ (i >> 1));
        while((int)ans.get(0) != start) ans.add(ans.remove(0));

        return ans;
    }
}
