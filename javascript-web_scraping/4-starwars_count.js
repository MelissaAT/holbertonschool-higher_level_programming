#!/usr/bin/node

const request = require('request');

function countMovies (url) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const moviesData = JSON.parse(body);
      const wedgeAntillesId = '18';

      let movieCount = 0;
      for (let i = 0; i < moviesData.results.length; i++) {
        const movie = moviesData.results[i];

        for (let j = 0; j < movie.characters.length; j++) {
          const characterUrl = movie.characters[j];
          if (characterUrl.includes(`/people/${wedgeAntillesId}/`)) {
            movieCount++;
            break;
          }
        }
      }

      console.log(movieCount);
    }
  });
}

const apiUrl = process.argv[2];

if (apiUrl) {
  countMovies(apiUrl);
}
