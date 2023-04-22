#!/usr/bin/node

const request = require('request');

function getTitle(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  });
}
const movieId = process.argv[2];
if (movieId) {
  getTitle(movieId);
}
