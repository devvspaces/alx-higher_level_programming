#!/usr/bin/node
const fs = require('fs');

const scraper = require('request');

scraper(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
