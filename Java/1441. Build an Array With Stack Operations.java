import java.util.Arrays;

class Solution {
    private int indexOf(int[] array, int target){
        for(int i = 0; i < array.length; i++){
            if(array[i] == target) return i;
        }
        return -1;
    }

    public List<String> buildArray(int[] target, int n) {
        List<String> ans = new ArrayList<>();

        for(int i = 1; i <= target[target.length - 1]; i++){
            if(indexOf(target, i) != -1) ans.add("Push");
            else{
                ans.add("Push");
                ans.add("Pop");
            }
        }

        return ans;
    }
}
