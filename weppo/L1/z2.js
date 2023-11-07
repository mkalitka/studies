function isDivisible(num){
    let sm = 0, cp_num = num;
    if(cp_num == 0) return false;

    while(cp_num > 0){
        if (cp_num % 10 == 0) return false;

        let figure = cp_num % 10;
        if(num % figure != 0) return false;
        
        sm += cp_num % 10;
        cp_num = Math.floor(cp_num / 10);
    }

    if(num % sm != 0) return false;
    
    return true;
}

function printDivNums(end){
    for(let i = 1; i < end; i++){
        if(isDivisible(i)){
            console.log(i);
        }
    }
}
printDivNums(100000)
