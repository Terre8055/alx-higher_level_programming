#!/usr/bin/node

const argv = require('process').argv;

const argOne = Number(argv[2]);

const argTwo = Number(argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(argOne, argTwo));
