#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(s.createWriteStream(process.argv[3]));
