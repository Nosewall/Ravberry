const container = document.getElementById("image-append");

var fs = require('fs');
var files = fs.readdirSync('/assets/photos/');

console.log(files);

