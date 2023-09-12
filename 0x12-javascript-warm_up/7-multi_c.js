#!/usr/bin/node

const arg = process.argv[2];

if (!arg || isNaN(arg)) {
  console.log('Missing number of occurrences');
}

const num = parseInt(arg);
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
