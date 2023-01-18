class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        List<Integer> ans = new ArrayList<Integer>();
        int temp;

        for(int i = 0; i < queries.length; i++){
            temp = 0;
            for(int j = 0; j < points.length; j++){
                if(Math.pow(queries[i][0] - points[j][0], 2) + Math.pow(queries[i][1] - points[j][1], 2) <= Math.pow(queries[i][2], 2)) temp += 1;
            }
            ans.add(temp);
        }

        int res[] = new int[ans.size()];
        for(int i = 0; i < ans.size(); i++) res[i] = (int)ans.get(i);
        return res;
    }
}
