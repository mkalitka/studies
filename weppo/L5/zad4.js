const fs = require('fs');

const readFile = new Promise((resolve, reject) => {
    fs.readFile('lorem.txt', 'utf-8', (error, data) => {
        if (error) {
          reject(error);
        }
        resolve(data);
    });
});

readFile.then((data) => {
  console.log(data);
});
