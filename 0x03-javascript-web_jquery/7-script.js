// This function will execute once the document is ready and all elements have been loaded
$(document).ready(function () {
  // This code will make a GET request to the SWAPI API to retrieve information about a specific character
  // The retrieved data will be passed as an argument to the callback function
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  // This line of code will update the text of the element with the ID 'character' to the name of the character
    $('#character').text(data.name);
  });
});
