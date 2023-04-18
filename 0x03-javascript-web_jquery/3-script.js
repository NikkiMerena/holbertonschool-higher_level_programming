// Wait for the document to be ready
$(document).ready(function () {
  // Add click event handler to the element with id "red_header"
  $('#red_header').click(function () {
  // Add the "red" class to the header element
    $('header').addClass('red');
  });
});
