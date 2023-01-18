class Solution {
    public int differenceOfSum(int[] nums) {
        int s1 = 0, s2 = 0;

        for(int i: nums){
            s1 += i;
            for(char j: String.valueOf(i).toCharArray()) s2 += (int)j - 48;
        }

        return Math.abs(s1 - s2);
    }
}
