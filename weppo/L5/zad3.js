const random = Math.floor(Math.random() * 100) + 1;

let i = 0;
process.stdout.write("Podaj liczbę: ");
process.stdin.on("data", (data) => {
    let input = parseInt(data.toString().trim());
    if (input) {
        i++;
        if (input === random) {
            console.log("Wygrałeś!");
            console.log("Liczba prób: " + i);
            process.exit();
        } else if (input > random) {
            console.log("Za dużo!");
        } else {
            console.log("Za mało!");
        }
    }
    process.stdout.write("Podaj liczbę: ");
});
