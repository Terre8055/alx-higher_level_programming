#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'x';
      }
      console.log(line);
    }
  }
};
