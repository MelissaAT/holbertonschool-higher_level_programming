#!/usr/bin/node

const args = parseInt(process.argv[2]);

let count = 0;

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  while (count < (args)) {
    count++;
    console.log('C is fun');
  }
}
