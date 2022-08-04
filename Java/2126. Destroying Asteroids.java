class Solution {
    public boolean asteroidsDestroyed(long mass, int[] asteroids) {
        Arrays.sort(asteroids);
        for(int i: asteroids){
            if(i <= mass){mass += i;}
            else{return false;}
        }
        return true;
    }
}
