#!/usr/bin/node
const myArray = process.argv;
if (myArray.length <= 3) {
  console.log(0);
} else {
  console.log(myArray.sort((a, b) => b - a).slice(3)[0]);
}
