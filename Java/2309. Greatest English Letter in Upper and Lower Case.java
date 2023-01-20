class Solution {
    public String greatestLetter(String s) {
//         char m = ' ';

//         for(char i: s.toCharArray()){
//             if(s.indexOf(i + 32) != -1 && i > m) m = i;
//         }

//         return String.valueOf(m == ' ' ? "" : m);

        for(char i = 'Z'; i >= 'A'; i--){
            if(s.indexOf(i) != -1 && s.indexOf(i + 32) != -1) return i + "";
        }

        return "";
    }
}
