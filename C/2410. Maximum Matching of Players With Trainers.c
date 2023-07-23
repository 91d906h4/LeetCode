int comp(const void* a, const void* b) {
    int t1 = *(int*)a, t2 = *(int*)b;

    if (t1 > t2) return 1;
    else if (t1 < t2) return -1;
    return 0;
}

int matchPlayersAndTrainers(int* players, int playersSize, int* trainers, int trainersSize){
    int res = 0;
    int i = 0, j = 0;

    qsort(players, playersSize, sizeof(int), comp);
    qsort(trainers, trainersSize, sizeof(int), comp);

    while (i < playersSize && j < trainersSize) {
        if (*(players + i) <= *(trainers + j)) {
            i++;
            res++;
        }

        j++;
    }

    return res;
}
