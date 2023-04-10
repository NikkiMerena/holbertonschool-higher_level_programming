#!/usr/bin/node

const [arg1] = process.argv.slice(2);

const num = parseInt(arg1);

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
