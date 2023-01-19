import java.util.Arrays;

class Solution {
    public int findMinFibonacciNumbers(int k) {
        int res = 0;
        List<Integer> fib = new ArrayList<>();
        fib.add(1); fib.add(1);

        while(fib.get(fib.size() - 1) < k) fib.add(fib.get(fib.size() - 1) + fib.get(fib.size() - 2));
        while(k > 0){
            for(int i = fib.size() - 1; i >= 0; i--){
                if(fib.get(i) <= k){
                    k -= fib.get(i);
                    res++;
                }
            }
        }

        return res;
    }
}
