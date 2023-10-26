#!/usr/bin/node

const fetcher = require('request');

const requestUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacter (error, _, body1) {
  if (error) {
    console.log(error);
  }
  const data1 = JSON.parse(body1);
  console.log(data1.name);
}

function callback (error, _, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    fetcher.get(i, getCharacter);
  }
}

fetcher.get(requestUrl, callback);
