#!/usr/bin/node
function Factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return (Factorial(n - 1) * n);
}
console.log(Factorial(Number(process.argv[2])));
