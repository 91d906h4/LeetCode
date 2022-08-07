function fib(n: number): number {
    var fib: Array<number> = [0, 1];
    for(var i = 2; i <= n; i++){
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
};
