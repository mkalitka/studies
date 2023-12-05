const fs = require('fs');
const https = require('https');

const options = {
    pfx: fs.readFileSync('cert.pfx'),
    passphrase: '1234',
};

https.createServer(options, (req, res) => {
    res.writeHead(200);
    res.end('Hello world!\n');
}).listen(8443);
