class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int temp[] = new int[26], t;

        for(int i = 0; i < s.length(); i++){
            t = (int)s.charAt(i) - 97;
            if(temp[t] == 0) temp[t] = i + 1;
            else if(i - temp[t] != distance[t]) return false;
        }

        return true;
    }
}
