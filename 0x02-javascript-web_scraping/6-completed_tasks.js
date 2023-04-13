#!/usr/bin/node

// Load the request module
const request = require('request');

// Send an HTTP GET request to the specified URL
request(process.argv[2], function (err, response, body) {
  // If an error occurred while sending the request, print the error to the console
  if (err) {
    console.log(err);
  } else {
    // Initialize an empty object to store the number of completed tasks per user
    const completedTasks = {};

    // Parse the response body into a JavaScript object
    const data = JSON.parse(body);

    // Iterate over the tasks in the response data and count the number of completed tasks per user
    for (let i = 0; i < data.length; i++) {
      // Get the user ID and completion status for the current task
      const userId = data[i].userId;
      const complete = data[i].completed;

      // If the task is complete, increment the count of completed tasks for the user in the completedTasks object
      if (complete) {
        if (!completedTasks[userId]) {
          completedTasks[data[i].userId] = 1;
        } else {
          completedTasks[data[i].userId] += 1;
        }
      }
    }

    // Print the completedTasks object to the console
    console.log(completedTasks);
  }
});
