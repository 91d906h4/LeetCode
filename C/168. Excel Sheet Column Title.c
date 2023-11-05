char* convertToTitle(int columnNumber) {
    char* res = (char*)malloc(1024 * sizeof(char));
    int pointer = 0, temp;

    while (columnNumber > 0) {
        temp = columnNumber % 26;
        if (temp == 0) {
            temp = 26;
            columnNumber -= 26;
        }

        *(res + pointer++) = (char)('A' + temp - 1);
        columnNumber /= 26;
    }

    *(res + pointer) = '\0';

    temp = strlen(res) - 1;
    for (int i = 0; i <= temp / 2; i++) {
        char c = *(res + i);
        *(res + i) = *(res + temp - i);
        *(res + temp - i) = c;
    }

    return res;
}
