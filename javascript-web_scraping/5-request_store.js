#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function saveWebpage (url, filePath) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

const url = process.argv[2];
const filePath = process.argv[3];

if (url && filePath) {
  saveWebpage(url, filePath);
}