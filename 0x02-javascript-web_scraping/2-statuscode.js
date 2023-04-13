#!/usr/bin/node
const request = require('request');

// Get the URL to request from the first command-line argument
const url = process.argv[2];

// Send a GET request to the specified URL
request.get(url, function (error, response) {
  if (error) {
    console.error('Error:', error);
  } else {
    // Print the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
