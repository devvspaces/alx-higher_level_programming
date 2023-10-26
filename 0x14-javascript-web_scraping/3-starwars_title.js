#!/usr/bin/node

const fetcher = require('request');

const baseUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

function callback (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
}

fetcher.get(baseUrl + movieId, callback);
