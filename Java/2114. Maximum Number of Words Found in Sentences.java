class Solution {
    public int mostWordsFound(String[] sentences) {
        int ans = 0, temp = 1;

        for(String i: sentences){
            temp = 1;

            for(char j: i.toCharArray()){
                if(j == ' ') temp++;
            }
            ans = Math.max(ans, temp);
        }

        return ans;
    }
}
