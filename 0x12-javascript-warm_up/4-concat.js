#!/usr/bin/node

const argv = require('process').argv;

const argOne = argv[2];

const argTwo = argv[3];

const concat = `${argOne} is ${argTwo}`;

console.log(concat);
