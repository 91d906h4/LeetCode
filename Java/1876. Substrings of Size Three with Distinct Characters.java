class Solution {
//     private int checkRepeat(String t){
//         int temp[] = new int[26];

//         for(char i: t.toCharArray()){
//             if(temp[(int)i - 97] != 0) return 1;
//             temp[(int)i - 97] = 1;
//         }

//         return -1;
//     }

//     public int countGoodSubstrings(String s) {
//         if(s.length() == 1) return 0;

//         int res = 0;
//         String t = "0" + s.substring(0, 2);

//         for(char i: s.substring(2, s.length()).toCharArray()){
//             t = t.substring(1, 3) + String.valueOf(i);
//             if(checkRepeat(t) == -1) res++;
//         }

//         return res;
//     }

        int res = 0;
        char a, b, c;

        for(int i = 0; i < s.length() - 2; i++){
            a = s.charAt(i);
            b = s.charAt(i + 1);
            c = s.charAt(i + 2);

            if(a != b && b != c && a != c) res++;
        }

        return res;
}
