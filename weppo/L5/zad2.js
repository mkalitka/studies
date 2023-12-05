process.stdout.write('Wpisz swoje imię: ');

process.stdin.setEncoding('utf-8');

process.stdin.on('readable', function() {
    var name = process.stdin.read();
    console.log('Witaj ' + name);
});
