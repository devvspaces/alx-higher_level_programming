#!/usr/bin/node
const fs = require('fs/promises');
const process = require('process');

// Extract paths from console arguments
const path1 = process.argv[2];
const path2 = process.argv[3];
const dest = process.argv[4];

// Read contents from paths and store to content
const contents = Promise.all([
  fs.readFile(path1, 'utf-8'),
  fs.readFile(path2, 'utf-8')
]);

// Write content to destination path
contents.then((content) => {
  fs.writeFile(dest, content[0] + content[1], (err) => {
    if (err) throw err;
    console.log('got here');
  });
});
