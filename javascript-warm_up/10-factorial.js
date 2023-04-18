#!/usr/bin/node
const args = process.argv[2];

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(args);

const result = factorial(num);
console.log(result);
