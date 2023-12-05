var http = require('https');

function fetch(url) {
    return new Promise((res, rej) => {
        http.get(url, function (resp) {
            var buf = '';
            resp.on('data', function (data) {
                buf += data.toString();
            });

            resp.on('end', function () {
                res(buf);
            });

            resp.on('error', function (err) {
                rej(err);
            });
        });
    });
}

fetch("https://www.example.com").then(data => (
    console.log(data)
));
