"use strict";
// Zaimplementuj funkcję fib(n) oraz drugą wersję fib_mem(n) z memoizacją.
function fib(n) {
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}
function fib_mem(n) {
    let memo = [];
    return fib_mem_helper(n, memo);
}
function fib_mem_helper(n, memo) {
    if (n < 2) {
        return n;
    }
    if (memo[n] !== undefined) {
        return memo[n];
    }
    memo[n] = fib_mem_helper(n - 1, memo) + fib_mem_helper(n - 2, memo);
    return memo[n];
}
console.log(fib(10));
console.log(fib_mem(10));
