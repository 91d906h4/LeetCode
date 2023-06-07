int jump(int* nums, int numsSize){
    int t = 0, m = 0, res = 0;

    for (int i = 0; i < numsSize - 1; i++) {
        t = (t > i + nums[i]) ? t : nums[i] + i;

        if (i == m) {
            res++;
            m = t;
        }
    }

    return res;
}
