void sort(int* arr, int arrSize) {
    for (int i = 1; i < arrSize; i++) {
        int temp = arr[i], j = i;

        while (j > 0 && arr[j - 1] > temp) {
            arr[j] = arr[j - 1];
            j--;
        }

        arr[j] = temp;
    }
}

bool canMakeArithmeticProgression(int* arr, int arrSize){
    sort(arr, arrSize);

    int dif = arr[1] - arr[0];

    for (int i = 1; i < arrSize; i++) {
        if (arr[i] - arr[i - 1] != dif) return 0;
    }

    return 1;
}
