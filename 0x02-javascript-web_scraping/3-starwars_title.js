#!/usr/bin/node

// Load the request module for making HTTP requests
const request = require('request');

// Get the ID of the Star Wars movie to search for from the first command-line argument
const id = process.argv[2];

// Create the URL for the Star Wars API endpoint that corresponds to the movie with the given ID
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

// Send an HTTP GET request to the specified URL and print the title of the movie
request(url, function (err, response, body) {
  // If an error occurred while sending the request, throw the error
  if (err) throw err;
  
  // Extract the title of the movie from the response body and print it to the console
  console.log(JSON.parse(body).title);
});
