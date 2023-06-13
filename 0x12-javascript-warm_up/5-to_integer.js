#!/usr/bin/node

const argv = require('process').argv;

if (argv.length > 2) {
  const number = Number(argv[2]);
  if (!isNaN(number)) {
    console.log(`My number: ${number}`);
  }
}
