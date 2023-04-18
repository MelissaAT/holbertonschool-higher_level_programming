#!/usr/bin/node

const args = process.argv;

if (args.length === 3) {
  console.log(0);
} else if (args[2] === undefined) {
  console.log(0);
} else {
  let bigger, bigger2;

  const num1 = parseInt(args[2]);
  const num2 = parseInt(args[3]);

  if (num1 > num2) {
    bigger = num1;
    bigger2 = num2;
  } else {
    bigger = num2;
    bigger2 = num1;
  }

  for (let i = 4; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > bigger) {
      bigger2 = bigger;
      bigger = num;
    } else if (num > bigger2 && num !== bigger) {
      bigger2 = num;
    }
  }

  console.log(bigger2);
}
