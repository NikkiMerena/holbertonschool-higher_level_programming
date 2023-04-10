#!/usr/bin/node

let message;

const numArgs = process.argv.length;

if (numArgs <= 2) {
  message = 'No argument';
} else if (numArgs === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
