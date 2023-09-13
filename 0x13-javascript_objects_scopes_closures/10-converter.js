#!/usr/bin/node

function converter (base) {
  function func (num) {
    return num.toString(base);
  }
  return func;
}

exports.converter = converter;
