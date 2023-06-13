#!/usr/bin/node

const superSquare = require('./5-square');

module.exports = class Square extends superSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let line = '';
      for (let j = 0; j < this.size; j++) {
        line += c;
      }
      console.log(line);
    }
  }
};
