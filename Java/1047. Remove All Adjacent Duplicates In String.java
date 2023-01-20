class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> temp = new Stack<>();
        StringBuilder ans = new StringBuilder();

        for(char i: s.toCharArray()){
            if(temp.size() > 0 && i == temp.get(temp.size() - 1)) temp.pop();
            else temp.add(i);
        }

        for(char i: temp) ans.append(i);

        return ans.toString();
    }
}
