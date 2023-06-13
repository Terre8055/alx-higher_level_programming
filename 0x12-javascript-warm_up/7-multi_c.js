#!/usr/bin/node

const argv = require('process').argv;

let argTwo = argv[2];

if (argv.length > 2) {
  const number = Number(argv[2]);
  if (isNaN(number)) {
    console.log('Missing number of occurrences');
  }
}
while (argTwo) {
  const msg = 'C is fun';
  console.log(`${msg}`);
  argTwo -= 1;
}
