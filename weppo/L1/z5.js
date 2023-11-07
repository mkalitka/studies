function itFibonacci(n){
    var valueA = 1, valueB = 1;

    for(let i = 0; i < n-1; i++){
        let tmp = valueB;
        valueB = valueA + valueB;
        valueA = tmp;
    }

    return valueB;
}

function rekFibonacci(n){
    if(n < 0) return 0;
    if(n < 2) return 1;

    return rekFibonacci(n - 2) + rekFibonacci(n - 1);
}

function checkTimes(end){
    for(let i = 0; i < end; i++){
        console.log("Próba dla n = " + i);

        console.time("itFibo");
        itFibonacci(i);
        console.timeEnd("itFibo");

        console.time("rekFibo");
        rekFibonacci(i);
        console.timeEnd("rekFibo");
    }
}

checkTimes(100);

