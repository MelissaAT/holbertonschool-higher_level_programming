#!/usr/bin/node

const args = process.argv;

let count = 0;

while (count < parseInt(args[2])) {
    count++
    console.log('C is fun');
}
if (args[1]) {
  console.log('Missing number of occurrences')
}