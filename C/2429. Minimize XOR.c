int minimizeXor(int num1, int num2) {
    int num1_bits = 0, num2_bits = 0,
        num1_temp = num1, num2_temp = num2;

    while (num1_temp) {
        num1_bits += num1_temp % 2;
        num1_temp >>= 1;
    }

    while (num2_temp) {
        num2_bits += num2_temp % 2;
        num2_temp >>= 1;
    }

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
