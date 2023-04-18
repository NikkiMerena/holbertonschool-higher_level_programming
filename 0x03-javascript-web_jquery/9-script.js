$(document).ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    // Extract the hello translation from the response data
    const helloTranslation = data.hello;
    // Set the hello translation as the text content of the div element
    $('#hello').text(helloTranslation);
  });
});
