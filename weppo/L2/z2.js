// Podpunkt - 1
console.log("Podpunkt 1")
let zmienna = "Jest dobrze dobrze chłopaki robią";
console.log(zmienna.split(" "))
console.log(zmienna[0])

// Podpunkt - 2
console.log("Podpunkt 2")
const person = {
  name: "John",
  age: 30,
  1: 2
};

const keyObject = {
  
};

person[keyObject] = 12;
console.log(person[1]);
console.log(person[keyObject])
// Programista ma wpływ na klucz taki, 
// że może wybrać jakim typem danych może mieć dostęp do danej wartości

// Podpunkt 3
console.log("Podpunkt 3")
let tab = ["M", "i", "k", "o", "ł", "a", "j"];
let key = {
  fun() { return 1; }
};

console.log(tab["M"])
console.log(tab['2'])
console.log(tab[key.fun()])

tab["name"] = 12;
console.log(tab)

tab.length = 1;
console.log(tab);
tab.length = 12;
console.log(tab);
