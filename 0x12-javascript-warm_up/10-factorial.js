#!/usr/bin/node

const argv = require('process').argv;

const argOne = Number(argv[2]);

function factorial (num) {
  if (num < 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

console.log(factorial(argOne));
