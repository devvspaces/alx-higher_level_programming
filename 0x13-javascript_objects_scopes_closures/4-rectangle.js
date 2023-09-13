#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let y = 0; y < (this.width ?? 0); y += 1) {
      row += 'X';
    }
    for (let x = 0; x < (this.height ?? 0); x += 1) {
      console.log(row);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (this.width !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
