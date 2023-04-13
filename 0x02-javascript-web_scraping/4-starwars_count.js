#!/usr/bin/node

// Load the request module for making HTTP requests
const request = require('request');

// Get the URL of the Star Wars API endpoint from the first command-line argument
const url = process.argv[2];

// Send an HTTP GET request to the specified URL and count the number of movies in which Samuel L. Jackson appeared
request(url, function (err, response, body) {
  // If an error occurred while sending the request, throw the error
  if (err) throw err;

  // Parse the JSON response body into a JavaScript object and extract the movie data
  const data = JSON.parse(body).results;

  // Initialize a counter variable for the number of movies in which Samuel L. Jackson appeared
  let count = 0;

  // Iterate over the movies in the response data
  for (const movie in data) {
    // Get the list of characters for the current movie
    const chars = data[movie].characters;

    // Iterate over the characters in the current movie
    for (const char in chars) {
      // Check if the current character is played by Samuel L. Jackson
      if (chars[char].includes('/18/')) {
        // If so, increment the counter variable
        count++;
      }
    }
  }

  // Print the number of movies in which Samuel L. Jackson appeared to the console
  console.log(count);
});
