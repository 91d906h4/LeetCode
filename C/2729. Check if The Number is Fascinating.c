bool isFascinating(int n){
    int table[10] = {0};
    int temp;

    for (int i = 1; i <= 3; i++) {
        temp = i * n;
        while (temp) {
            table[temp % 10]++;
            temp /= 10;
        }
    }

    if (*table != 0)
        return false;

    for (int i = 1; i < 10; i++)
        if (table[i] != 1)
            return false;

    return true;
}
