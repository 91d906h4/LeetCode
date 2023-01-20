class Solution {
    public String removeStars(String s) {
        Stack<Character> temp = new Stack<>();
        StringBuilder ans = new StringBuilder();

        for(char i: s.toCharArray()){
            if(i == '*') temp.pop();
            else temp.add(i);
        }

        for(char i: temp) ans.append(i);

        return ans.toString();
    }
}
