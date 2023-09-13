#!/usr/bin/node

function nbOccurences (list, searchElement) {
  return list.filter((el) => searchElement === el).length;
}

exports.nbOccurences = nbOccurences;
