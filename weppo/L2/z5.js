const mojObiekt = {
    pole: 42,
    metoda: function() {
      console.log('To jest moja metoda.');
    },
    get mojaWlasciwosc() {
      return this.pole;
    },
    set mojaWlasciwosc(nowaNazwa) {
      this.pole = nowaNazwa;
    }
  };

console.log(mojObiekt.pole);

console.log(mojObiekt.mojaWlasciwosc);

// Dodawanie nowego pola
mojObiekt.nowePole = 21;

// Dodawanie nowej metody
mojObiekt.nowaMetoda = function() {
 console.log('To jest moja nowa metoda.');
};

// Dodawanie nowej właściwości z akcesorami get i set
Object.defineProperty(mojObiekt, 'nowaWl', {
  get: function() {
    return this.nowePole;
  },
  set: function(nowaNazwa) {
    nowaNazwa = this.nowePole;
    console.log("ustawiono nową wartoś pola", nowaNazwa)
  }
});


console.log(mojObiekt.nowaWl);
mojObiekt.nowaWl = 21;
console.log(mojObiekt.nowaWl)
console.log(mojObiekt.nowePole)
