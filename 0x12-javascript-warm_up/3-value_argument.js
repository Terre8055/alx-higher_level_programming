#!/usr/bin/node

const { argv } = require('node:process')

if (argv.length <= 2) {
  console.log('No Argument')
} else {
  console.log(argv[2])
}
