char nextGreatestLetter(char* letters, int lettersSize, char target){
    int t = (int)target;

    // for (int i = 0; i < lettersSize; i++) {
    //     if ((int)letters[i] > t) return letters[i];
    // }

    int l = 0, r = lettersSize - 1, m;

    while (l <= r) {
        m = (l + r) / 2;

        if ((int)letters[m] > t) r = m - 1;
        else l = m + 1;
    }

    if (l >= lettersSize) return letters[0];
    else return letters[l];
}
