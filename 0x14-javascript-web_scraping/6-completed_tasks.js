#!/usr/bin/node
const fetcher = require('request');

function callback (error, _, body) {
  if (!error) {
    const todo = JSON.parse(body);
    const completed = {};
    todo.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
}

fetcher(process.argv[2], callback);
