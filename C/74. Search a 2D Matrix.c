bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int i;

    for (i = 0; i < matrixSize; i++) {
        if (matrix[i][0] == target) return 1;
        else if (matrix[i][0] > target) break;
    }

    if (i-- == 0) return 0;

    for (int j = 0; j < *matrixColSize; j++) {
        if (matrix[i][j] == target) return 1;
    }

    return 0;
}
