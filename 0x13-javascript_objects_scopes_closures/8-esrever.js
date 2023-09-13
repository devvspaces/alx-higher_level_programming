#!/usr/bin/node

function esrever (list) {
  let l = 0;
  let r = list.length - 1;

  while (l < r) {
    [list[l], list[r]] = [list[r], list[l]];
    l += 1;
    r -= 1;
  }

  return list;
}

exports.esrever = esrever;
