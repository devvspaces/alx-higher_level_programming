#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

function callback (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
}

request(url, callback);
