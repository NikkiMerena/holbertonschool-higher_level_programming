#!/usr/bin/node
const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const n = parseInt(size);
  let row = '';
  for (let i = 0; i < n; i++) {
    row += 'X';
  }
  for (let i = 0; i < n; i++) {
    console.log(row);
  }
}
