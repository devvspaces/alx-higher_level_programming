#!/usr/bin/node

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    const char = c ?? 'X';
    let row = '';
    for (let y = 0; y < (this.width ?? 0); y += 1) {
      row += char;
    }
    for (let x = 0; x < (this.height ?? 0); x += 1) {
      console.log(row);
    }
  }
}

module.exports = Square;
