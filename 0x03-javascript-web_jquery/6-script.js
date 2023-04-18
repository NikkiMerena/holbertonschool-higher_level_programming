// This function will execute once the document is ready and all elements have been loaded
$(document).ready(function () {
  // This code will execute when the user clicks the element with the ID 'update_header'
  $('#update_header').click(function () {
  // This line of code will update the text of the 'header' element to 'New Header!!!'
    $('header').text('New Header!!!');
  });
});
