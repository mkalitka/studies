function* take(it, top) {
    for(let i = 0; i <= top; i++) {
        const { value, done } = it.next()
        if( done ) {
            break
        }
        yield value
    }
}

function* fibGen() {
    let a = 1, b = 1
    while(true) {
        yield a
        let c = a
        a = b
        b = b + c
    }
}

for (let num of take(fibGen(), 10)) {
    console.log(num);
}
