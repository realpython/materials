document.querySelector('#copy-button').addEventListener('click', () => {
  const colorCode = document.querySelector('#color-code').textContent;
  navigator.clipboard.writeText(colorCode);
});
