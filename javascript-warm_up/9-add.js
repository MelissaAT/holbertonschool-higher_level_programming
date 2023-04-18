#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log(NaN);
} else {
  const sum = parseInt(args[2]) + parseInt(args[3]);
  console.log(sum);
}
