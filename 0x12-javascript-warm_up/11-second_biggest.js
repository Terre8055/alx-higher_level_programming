#!/usr/bin/node

const argv = require('process').argv;

const filter = argv
  .slice(2)
  .filter((elem) => !isNaN(Number(elem)))
  .map(Number)
  .sort((a, b) => a - b);

console.log(filter[filter.length - 2]);
