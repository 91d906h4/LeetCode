class Solution {
    public int partitionString(String s) {
//         String temp = "";
//         int ans = 1;

//         for(char i: s.toCharArray()){
//             if(temp.indexOf(i) == -1) temp += i;
//             else{
//                 temp = String.valueOf(i);
//                 ans++;
//             }
//         }

//         return ans;

        int temp[] = new int[26], ans = 1, t;

        for(char i: s.toCharArray()){
            t = (int)i - 97;
            if(temp[t] == 0) temp[t] = 1;
            else{
                temp = new int[26];
                temp[t] = 1;
                ans++;
            }
        }

        return ans;
    }
}
