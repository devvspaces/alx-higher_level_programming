#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg, 10);

if (!arg || Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x += 1) {
    let row = '';
    for (let y = 0; y < size; y += 1) {
      row += 'X';
    }
    console.log(row);
  }
}
