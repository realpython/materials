document.querySelector('#copy-button').addEventListener('click', function() {
    const colorCode = document.querySelector('#color-code').textContent;
    navigator.clipboard.writeText(colorCode);
});
