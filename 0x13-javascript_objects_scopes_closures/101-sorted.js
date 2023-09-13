#!/usr/bin/node

const data = require('./101-data').dict;

const dict = {};

for (const key in data) {
  let dict_value = dict[data[key]] ?? [];
  dict_value.push(key);
  // dict_value.sort((a, b) => parseInt(a) - parseInt(b));
  dict[data[key]] = dict_value;
}

console.log(dict);
