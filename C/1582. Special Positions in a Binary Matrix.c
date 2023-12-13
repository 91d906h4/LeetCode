int r, c;

int check(int** mat, int i, int j) {
    if (!mat[i][j]) return 0;

    int temp = 0;

    for (int a = 0; a < r; a++) {
        if (mat[a][j]) temp++;
    }

    if (temp != 1) return 0;
    temp = 0;

    for (int b = 0; b < c; b++) {
        if (mat[i][b]) temp++;
    }

    if (temp != 1) return 0;

    return 1;
}

int numSpecial(int** mat, int matSize, int* matColSize) {
    r = matSize, c = *matColSize;
    int res = 0;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (check(mat, i, j)) res++;
        }
    }

    return res;
}
