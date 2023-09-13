#!/usr/bin/node

let num = 0;

function logMe (item) {
  console.log(`${num}: ${item}`);
  num += 1;
}

exports.logMe = logMe;
