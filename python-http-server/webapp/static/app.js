document.addEventListener("DOMContentLoaded", function() {
  const span = document.querySelector("#seconds");
  let numSeconds = 0;
  setInterval(function() {
    span.innerText = ++numSeconds;
  }, 1000);
});
