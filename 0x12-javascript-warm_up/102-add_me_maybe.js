#!/usr/bin/node

function addMeMaybe (times, func) {
  let num = times;
  num += 1;
  func(num);
}

exports.addMeMaybe = addMeMaybe;
