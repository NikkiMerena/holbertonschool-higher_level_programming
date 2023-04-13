#!/usr/bin/node

// Load the fs module for working with the file system
const fs = require('fs');

// Read the file specified by the user in the command-line argument
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  // If an error occurred while reading the file, log the error to the console
  if (err) {
    console.log(err);
  } else {
    // If the file was read successfully, log its contents to the console
    console.log(data);
  }
});
