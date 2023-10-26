#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];
const content = process.argv[3];

function errorHandler (err) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(file, content, 'utf-8', errorHandler);
