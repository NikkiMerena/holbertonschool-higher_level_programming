#!/usr/bin/node

// Define the `$` variable as an alias for the `$` symbol in the global `window` object
const $ = window.$;

// Select the <header> element using jQuery and set its text color to red (#F00)
$('header').css('color', '#F00');
