class Solution {
    public int minPartitions(String n) {
        int ans = 0;

        for(char i: n.toCharArray()) ans = Math.max(ans, (int)i - 48);
    
        return ans;
    }
}
