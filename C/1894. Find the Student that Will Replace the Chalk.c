int chalkReplacer(int* chalk, int chalkSize, int k){
    long long sum = 0, pointer = 0;

    for (int i = 0; i < chalkSize; i++) sum += *(chalk + i);

    k %= sum;

    while (k > 0) {
        long long temp = *(chalk + pointer++);

        if (k < temp) return --pointer;
        else k -= temp;
    }

    return pointer;
}
