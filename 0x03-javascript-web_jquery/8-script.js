$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  // Loop through each movie in the results
    data.results.forEach(function (movie) {
      // Create a new list item element
      const listItem = $('<li>').text(movie.title);
      // Append the list item to the unordered list
      $('#list_movies').append(listItem);
    });
  });
});
