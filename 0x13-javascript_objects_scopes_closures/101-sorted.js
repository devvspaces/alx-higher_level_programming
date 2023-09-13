#!/usr/bin/node

const data = require('./101-data').dict;

const dict = {};

for (const key in data) {
  const dictValue = dict[data[key]] ?? [];
  dictValue.push(key);
  // dict_value.sort((a, b) => parseInt(a) - parseInt(b));
  dict[data[key]] = dictValue;
}

console.log(dict);
