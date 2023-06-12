#!/usr/bin/node

const { argv } = require('node:process')

const argOne = argv[2]

const argTwo = argv[3]

const concat = `${argOne} is ${argTwo}`

console.log(concat)
