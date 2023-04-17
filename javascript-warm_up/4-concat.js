#!/usr/bin/node

const args = process.argv;

const str = args[2];
const str1 = args[3];

if (args[2]) {
  console.log(str, ' is ', str1);
} else if (args[3]) {
  console.log(str, ' is ', str1);
} else {
  console.log('undefined is undefined');
}
