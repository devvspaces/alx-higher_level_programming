#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
  process.exit(0);
}

for (let i = 0; i < args.length; i += 1) {
  args[i] = parseInt(args[i], 10);
}

args.sort((a, b) => a - b);
console.log(args[args.length - 2]);
