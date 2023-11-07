function forEach(a, f) {
    for (let i = 0; i < a.length; i++) {
        f(a[i])
    }
}

function map(a, f) {
    let result = []
    for (let i = 0; i < a.length; i++) {
        result.push(f(a[i]))
    }
    return result
}

function filter(a, f) {
    let result = []
    for (let i = 0; i < a.length; i++) {
        if (f(a[i])) {
            result.push(a[i])
        }
    }
    return result;
}

var a = [1, 2, 3, 4]

console.log("forEach:");
forEach(a, _ => { console.log(_) })

console.log("filter:")
console.log(filter(a, _ => _ < 3))

console.log("map:")
console.log(map(a, _ => _ * 2))
