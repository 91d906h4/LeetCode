int maxProfit(int* prices, int pricesSize){
    int m = 0, t = *prices;

    for (int i = 0; i < pricesSize; i++) {
        if (*(prices + i) < t) {
            t = *(prices + i);
        }
        if (*(prices + i) - t > m) {
            m = *(prices + i) - t;
        }
    }

    return m;
}
