'use strict';

let helloButton = document.getElementById("hello-btn");

helloButton.onclick = function (element) {
  const defaultName = "Real JavaScript";
  let name = prompt("Enter your name:", defaultName);
  if (!name) {
    name = defaultName;
  }
  document.getElementById("hello").innerHTML = `Hello, ${name}!`;
};
