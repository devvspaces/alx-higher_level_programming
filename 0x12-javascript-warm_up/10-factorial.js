#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const arg1 = process.argv[2];
let num = parseInt(arg1, 10);

if (Number.isNaN(num)) {
  num = 0;
}

console.log(factorial(num));
