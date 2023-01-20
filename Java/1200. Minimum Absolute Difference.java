class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> ans = new ArrayList<>();
        int min = 10001, l = arr.length;

        Arrays.sort(arr);
        
        for(int i = 0; i < l - 1; i++) min = Math.min(min, arr[i + 1] - arr[i]);
        for(int i = 0; i < l - 1; i++){
            if(arr[i + 1] - arr[i] == min) ans.add(Arrays.asList(arr[i], arr[i + 1]));
        }

        return ans;
    }
}
