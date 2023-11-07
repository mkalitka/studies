function fib() {
    let a = 1, b = 1
    return {
        next : function() {
            let c = a
            a = b
            b = a + c
            return {
                value : c,
                done : false
            }
        }
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

var _it = fib();
for ( var _result; _result = _it.next(), !_result.done; ) {
    console.log( _result.value )
    if (_result.value > 1000) break
}

var _it = fibGen();
for ( var _result; _result = _it.next(), !_result.done; ) {
    console.log( _result.value )
    if (_result.value > 1000) break
}

for (var f of fibGen()) {
    console.log(f)
    if(f > 1000) break
}
