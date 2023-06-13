#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  if (x) {
    let start = 0
    while (start < x) {
      theFunction()
      start += 1
    }
  }
}
