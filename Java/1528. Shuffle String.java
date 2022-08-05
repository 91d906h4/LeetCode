class Solution {
    public String restoreString(String s, int[] indices) {
//         String[] r = new String[s.length()];
//         for(int i = 0; i< s.length(); i++){
//             r[indices[i]] = String.valueOf(s.charAt(i));
//         }
//         return String.join("", r);

        StringBuilder r = new StringBuilder(s);
        for(int i = 0; i < s.length(); i++){
            r.setCharAt(indices[i], s.charAt(i));
        }
        return r.toString();
    }
}
