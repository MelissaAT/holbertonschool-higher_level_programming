#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === undefined || this.height === undefined) {
      return; // Don't print anything if the object is empty
    }

    const line = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Rectangle;
