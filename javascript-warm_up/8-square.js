#!/usr/bin/node

const args = process.argv;

const size = parseInt(args[2]);

if (isNaN(size)) {
  console.log('Missin size');
}
const msg = 'X';

for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += msg;
  }
  console.log(row);
}
