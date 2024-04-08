#!/usr/bin/node
const number = process.argv[2];
if (number === undefined || isNaN(number)) {
  console.log('Missing size');
} else {
  const x = Number(number);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
