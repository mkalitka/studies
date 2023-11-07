var memoFib = {
    cache: {},
    fib: function(n) {
        if (n in this.cache) {
            return this.cache[n];
        }
        else {
            if (n < 2) {
                return n;
            }
            else {
                this.cache[n] = this.fib(n - 1) + this.fib(n - 2);
                return this.cache[n];
            }
        }
    }
}

for (let i = 0; i < 100; i++) {
    console.time()
    console.log("n = " + i + "\nfib(" + i + ") = " + memoFib.fib(i));
    console.timeEnd()
}
