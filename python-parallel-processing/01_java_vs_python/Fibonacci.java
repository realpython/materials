public class Fibonacci {
    public static void main(String[] args) {
        int cpus = Runtime.getRuntime().availableProcessors();
        for (int i = 0; i < cpus; i++) {
            new Thread(() -> fib(45)).start();
        }
    }
    private static int fib(int n) {
        return n < 2 ? n : fib(n - 2) + fib(n - 1);
    }
}

