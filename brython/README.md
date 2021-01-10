# Brython Examples

This set of example is intended to accompany the [Real Python](https://realpython.com/) tutorial [Brython: Python in Your Browser](https://realpython.com/brython-python-in-browser).

Most of the examples are lined in the article and others are more complete examples going beyond the scope of the Brython tutorial.

## async

* Project demonstrating how to use Brython asynchronous functions to request data from a server API.
* In the following examples, the API is a simple text file that returns the text "Real Python"
* To test the examples, execute a local web server in the respective directory
* The recommended Python development server is started with: `python -m http.server`

### aio

* Demonstrates the usage of `browser.aio` the substitute to `asyncio` in Brython.
* https://www.brython.info/static_doc/en/aio.html

### ajax

* Demonstrates the usage of `browser.ajax`.
* https://www.brython.info/static_doc/en/ajax.html

### fetch

* Demonstrates the usage of JavaScript `fetch` from Brython.
* https://www.brython.info/static_doc/en/ajax.html

## base64

Examples demonstrating how to access the DOM API starting from an app that takes a string as input, generates the base64 encoded value of the string, and displays it on the page. Each example is slightly different as stated in the following sections.

### embed

The application is a single `index.htm` with embedded Python code. It can be executed by opening the file with an internet browser. Starting a local web server is not required.

The user enters the string to be encoded through the standard prompt message box of the browser.

### form

The application is an `index.html` with the Python code in a separate `main.py` file. Starting a local webserver is required (`python3 -m http.server`).

The user enters the string in the HTML form of the main page.

### sep

This project is the same as `embed` but the Python code is a separate file, `main.py`. A separate Python file requires to start a local server to test this example (`python3 -m http.server`)

### storage

This example is an extension of the **form** project demonstrating how to use `localstorage` and save the data between page reload. It requires to start a local web server (`python3 -m http.server`).

The data is saved as a JSON document associated with a single key of the local storage. The performance is degrading as you add more elements in the JSON file.

### storate_perf

In an attempt to overcome the performance issue of the `storage` example, this example saves each base64 encoded value into a separate key. The key is the original string entered by the user.

## chrome_extensions

### hello_js

Example of a JavaScript Google Chrome extension.

### hello_py

Same example as hello_js using Brython.

## console

Brython console as an iframe embedded in an HTML file. Does not require to run a local web server. Opening `index.html` with a browser is sufficient to test it.

## github_install

`index.html` loading the Brython engine from GitHub. You can open the file directly. It only displays a message box with "Hello Real Python".

## hashes

In the same vein as the Base 64 encode application, this one generate the hash, SHA-1, SHA-256 or SHA-512, of a string. It adds a dropdown to select the desired algorithm (SHA-1, SHA-256, or SHA-512).

This serves as the basis for a translation to the same application with Vue.js (see **vuejs** project below).

It requires a local webserver.

## import

Shows how to import an external Python module. The external module is `functional.py`. The main Python code is embedded in the HTML page.

It requires a local webserver.

## import_js

Expands on the `import` example by allowing the creation of `brython_module.js` generated with `brython-cli --modules`.

This requires a Python virtual environment with Brython installed (`pip install brython`) to have `brython-cli` available in the PATH. The generated files are available in the sub-directory `dist_example`.

You can open `dist_example/index.html` with a browser, without the need for a webserver to run locally, because the dependencies are only JS files (`brython.js` and `brython_modules.js`).

## npm_install

Example of a Brython project installed with `npm`. See the corresponding tutorial section for more details.

## pip_install

Example of a Brython project installed with `pip`. See the corresponding tutorial section for more details.

## sha256

Application to generate the SHA-256 hash of a given string. The data is stored as JSON in a key of the localstorage to preserver the calculations between page reloads.

## vuejs

Brython and Vue.js implementation of `hashes`. Requires a local webserver to be running.

## wasm

An example demonstrating the generation of a WASM file, the loading of the file, and usage of the function from Brython. The source code of the WASM file is Rust.

This requires to have the Rust compiler installed on a local machine. Check the detail in the Brython tutorial. A local webserver is needed as it requires to load the wasm file.

The web server can be started in the directory `wasm/op/web`. The debug wasm file is included. This is only for demonstration. The `add` function does not handle negative and big integers.

## zero_install

An example demonstrating a minimum Brython project. The Brython engine is fetched from a CDN, and the Python code is embedded on the page. No need for a local web server, no need for a local Python environment either, just a browser with JavaScript enabled :-)
