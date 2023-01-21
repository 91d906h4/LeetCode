class Solution {
    public int countCharacters(String[] words, String chars) {
        int ans = 0, flag;
        HashMap<Character, Integer> dict = new HashMap<>(), temp = new HashMap<>();

        for(char i: chars.toCharArray()) dict.put(i, (dict.get(i) == null ? 1 : dict.get(i) + 1));

        for(String i: words){
            temp.putAll(dict);
            flag = 1;

            for(char j: i.toCharArray()){
                if(temp.get(j) == null || temp.get(j) == 0){
                    flag = 0;
                    break;
                }
                temp.put(j, (temp.get(j) - 1));
            }

            if(flag == 1) ans += i.length(); 
        }

        return ans;
    }
}
