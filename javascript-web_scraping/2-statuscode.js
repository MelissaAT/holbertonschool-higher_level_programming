#!/usr/bin/node

const request = require('request');

function getRequest (url) {
  request(url, (error, response) => {
    if (!error) {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
const url = process.argv[2];
if (url) {
  getRequest(url);
}
