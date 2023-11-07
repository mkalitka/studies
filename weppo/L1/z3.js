function isPrime(num){
    if(num == 1 || num == 0) return false;
    
    for(let i = 2; i < num; i++){
        if(num % i == 0) return false;
    }
    return true;
}

function range_of_primes(end){
    var lst = [2];
    for(let i = 3; i < end; i += 2){
        if(isPrime(i)){
            lst.push(i);
        }
    }
    return lst.join(" ");
}
console.log(range_of_primes(100000));