class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){return false;}
        String s = String.valueOf(x);
        int l = s.length() - 1;
        for(int i = 0; i < l / 2 + 1; i++){
            if(s.toCharArray()[i] != s.toCharArray()[l - i]){return false;}
        }
        return true;
    }
}
