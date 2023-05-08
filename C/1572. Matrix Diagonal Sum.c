int diagonalSum(int** mat, int matSize, int* matColSize){
    int res = 0;
    int c = matSize;

    for (int i = 0; i < c;i ++) {
        res += mat[i][i] + mat[c - 1 - i][i];
    }

    if (matSize % 2) res -= mat[matSize / 2][matSize / 2];

    return res;
}
