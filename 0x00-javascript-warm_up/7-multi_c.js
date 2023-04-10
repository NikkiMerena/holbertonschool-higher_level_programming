#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let message = '';
  for (let i = 0; i < x; i++) {
    message += 'C is fun\n';
  }
  console.log(message.trim());
}
