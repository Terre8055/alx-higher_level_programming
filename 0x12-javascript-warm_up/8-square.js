#!/usr/bin/node

const argv = require('process').argv;

const argTwo = Number(argv[2]);

if (!isNaN(argTwo)) {
  for (let i = 0; i < argTwo; i++) {
    let line = '';
    for (let y = 0; y < argTwo; y++) {
      line += 'x';
    }
    console.log(line);
  }
}
