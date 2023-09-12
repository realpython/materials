int fib(int n) {
    return n < 2 ? n : fib(n - 2) + fib(n - 1);
}
