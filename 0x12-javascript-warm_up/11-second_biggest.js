#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let smax = -Infinity;

  for (const num of args) {
    if (num < max && num > smax) {
      smax = num;
    }
  }
  console.log(smax);
}
