#!/usr/bin/node

// Load the fs module for working with the file system
const fs = require('fs');

// Write the data specified by the user to the file specified by the user
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  // If an error occurred while writing the file, throw the error
  if (err) throw err;
});
