#!/usr/bin/node

function callMeMoby (times, func) {
  for (let i = 0; i < times; i += 1) {
    func();
  }
}

exports.callMeMoby = callMeMoby;
