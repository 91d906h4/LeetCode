class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int X = 0;

        for(String i: operations){
            if(i.equals("X++") || i.equals("++X")) X++;
            else X--;
        }

        return X;
    }
}
