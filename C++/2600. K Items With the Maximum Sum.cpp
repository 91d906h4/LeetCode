class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int temp = k - numOnes - numZeros;
        if (temp <= 0) return min(k, numOnes);
        else return numOnes - temp;
    }
};
