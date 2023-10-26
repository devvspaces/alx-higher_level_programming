#!/usr/bin/node
const request = require('request');

function callback (error, response, body) {
  if (!error) {
    const data = Array.from(JSON.parse(body).results);
    console.log(
      data.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0)
    );
  }
}

request(process.argv[2], callback);
