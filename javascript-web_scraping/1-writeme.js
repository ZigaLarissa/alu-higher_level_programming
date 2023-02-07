#!/usr/bin/node
let myFile = process.argv[2];
let content = process.argv[3];
const fs = require('fs');
fs.writeFile(myFile, content, err => {
  if (err) {
    console.log(err);
    return;
  }

});
