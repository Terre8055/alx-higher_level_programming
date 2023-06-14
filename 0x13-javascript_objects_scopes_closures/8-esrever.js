#!/usr/bin/node

exports.esrever = function (list) {
  const result = [...list];

  let startPos = 0;
  let endPos = result.length - 1;

  while (startPos < endPos) {
  	const tempIndex = result[startPos];
  	result[startPos] = result[endPos];
  	result[endPos] = tempIndex;
  	startPos += 1;
  	endPos -= 1;
  }
  return result;
};
