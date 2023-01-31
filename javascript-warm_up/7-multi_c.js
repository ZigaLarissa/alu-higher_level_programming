#!/usr/bin/node
const firstArgv = process.argv[2];
if (isNaN(firstArgv)) { console.log('Missing number of occurrences'); } else {
  for (let i = 0; i < firstArgv; i++) { console.log('C is fun'); }
}
