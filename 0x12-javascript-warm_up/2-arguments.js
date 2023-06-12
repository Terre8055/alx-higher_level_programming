#!/usr/bin/node

const { argv } = require('node:process')

if (argv.length <= 2) {
  console.log('No Argument')
} else if (argv.length === 3) {
  console.log('Argument Found')
} else if (argv.length > 3) {
  console.log('Arguments Found')
}
