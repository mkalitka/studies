function sum(...args) {
    let s = 0
    for (let i = 0; i < args.length; i++) {
        s += args[i]
    }
    return s
}

console.log(sum(1, 2, 4, 3, -2))
console.log(sum(1, 2, 4, 3, -2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
