#!/usr/bin/node
const childsquare = require('./5-square');

class Square extends childsquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
