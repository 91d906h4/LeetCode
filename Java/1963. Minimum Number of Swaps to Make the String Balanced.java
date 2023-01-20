class Solution {
    public int minSwaps(String s) {
//         Stack<Character> temp = new Stack<>();

//         for(char i: s.toCharArray()){
//             if(i == ']' && temp.size() > 0 && temp.lastElement() == '[') temp.pop();
//             else temp.push(i);
//         }

//         return (temp.size() + 2) / 4;

        int ans = 0;
        for(char i: s.toCharArray()){
            if(i == '[') ans++;
            else if(ans > 0) ans--;
        }

        return (ans + 1) / 2;
    }
}
