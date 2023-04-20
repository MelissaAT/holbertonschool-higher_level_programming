#!/usr/bin/node

const fs = require('fs');

function readFiles (filepath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) throw err;
    console.log(data);
  });
}
const filePath = process.argv[2];
readFiles(filePath);
