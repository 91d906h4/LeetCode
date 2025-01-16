int count_bits(int num) {
    int bits = 0;

    while (num) {
        bits += num % 2;
        num >>= 1;
    }

    return bits;
}

int minimizeXor(int num1, int num2) {
    int num1_bits = count_bits(num1), num2_bits = count_bits(num2);

    int diff = num1_bits - num2_bits;

    if (diff == 0) {
        return num1;
    } else if (diff > 0) {
        while (diff--) num1 &= (num1 - 1);

        return num1;
    } else {
        int temp = 0;
        diff = num2_bits - num1_bits;

        while (diff) {
            while ((num1 >> temp) & 1) temp++;

            num1 |= (1 << temp);
            diff--;
        }

        return num1;
    }

    return -1;
}
