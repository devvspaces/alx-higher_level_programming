#!/usr/bin/node
const fs = require('fs');

const handler = (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
};

fs.readFile(process.argv[2], 'utf-8', handler);
