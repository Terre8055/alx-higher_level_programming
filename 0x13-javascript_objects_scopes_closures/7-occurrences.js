#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const getFiltered = list.filter((elem) => elem === searchElement);

  return getFiltered.length;
};
