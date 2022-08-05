class Solution {
    public String restoreString(String s, int[] indices) {
        String[] r = new String[s.length()];
        for(int i = 0; i< s.length(); i++){
            r[indices[i]] = String.valueOf(s.charAt(i));
        }
        return String.join("", r);
    }
}
