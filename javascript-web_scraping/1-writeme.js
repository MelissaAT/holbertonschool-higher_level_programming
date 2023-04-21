#!/usr/bin/node

const fs = require('fs');

function writeFiles (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) throw err;
    console.log(err);
  });
}
const filePath = process.argv[2];
const content = process.argv[3];
writeFiles(filePath, content);
