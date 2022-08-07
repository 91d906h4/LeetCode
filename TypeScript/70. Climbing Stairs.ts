function climbStairs(n: number): number {
    var t: Array<number> = [1, 1];
    for(var i = 2; i <= n; i++){
        t[i] = t[i - 1] + t[i - 2];
    }
    return t[n];
};
