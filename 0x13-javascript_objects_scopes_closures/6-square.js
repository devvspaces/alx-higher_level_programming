#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
