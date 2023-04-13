#!/usr/bin/node

// Load the request and fs modules
const request = require('request');
const fs = require('fs');

// Send an HTTP GET request to the URL specified in the second command-line argument
request(process.argv[2], function (err, response, body) {
  // If an error occurred while sending the request, print the error to the console
  if (err) {
    console.log(err);
  } else {
    // Append the response body to the file specified in the third command-line argument
    fs.appendFile(process.argv[3], body, function (writeError) {
      // If an error occurred while writing to the file, print the error to the console
      if (writeError) {
        console.log(writeError);
      }
    });
  }
});
