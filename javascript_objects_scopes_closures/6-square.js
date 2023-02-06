#!/usr/bin/node
const Sq = require('./5-square.js');
class Square extends Sq {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
