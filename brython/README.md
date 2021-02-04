# Brython Examples

This set of examples is intended to accompany the [Real Python](https://realpython.com/) tutorial [Brython: Python in Your Browser](https://realpython.com/brython-python-in-browser).

Most of the examples are found in the article and others are extras that did not fit in the scope of the article.

## async

* Project demonstrating how to use Brython asynchronous functions to request data from a server API
* In the following examples, the API is a simple text file that returns the text "Real Python"
* To test the examples, execute a local web server in the respective directory
* The recommended Python development server is started with: `python -m http.server`
* https://realpython.com/brython-python-in-browser/#applying-asynchronous-development-in-brython

### aio

* Demonstrates the usage of `browser.aio`, the substitute to `asyncio` in Brython
* This example is in the tutorial: https://realpython.com/brython-python-in-browser/#async-io-in-brython
* https://www.brython.info/static_doc/en/aio.html

### ajax

* Demonstrates the usage of `browser.ajax`
* This example is in the tutorial: https://realpython.com/brython-python-in-browser/#ajax-in-brython
* https://www.brython.info/static_doc/en/ajax.html

### fetch

* Demonstrates the usage of JavaScript `fetch` from Brython
* This example is not in the tutorial and is provided as an extra. It is related to this section: https://realpython.com/brython-python-in-browser/#applying-asynchronous-development-in-brython

## Base64

Examples demonstrating how to access the DOM API starting from an app that takes a string as input, generates the Base64-encoded value of the string, and displays it on the page. Each example is slightly different as stated in the following sections.

### embed

* The application is a single `index.htm` with embedded Python code. It can be executed by opening the file with an internet browser. Starting a local web server is not required
* The user enters the string to be encoded through the standard prompt message box of the browser.
* This example is the same as the following one but with the Python code embedded in HTML.
* It is not in the tutorial in this format, but relates to https://realpython.com/brython-python-in-browser/#the-dom-api-in-brython

### sep

* This project is the same as `embed`, but the Python code is a separate file, `main.py`. 
* A separate Python file requires starting a local server to test this example (`python3 -m http.server`).

### form

* The application is an `index.html` with the Python code in a separate `main.py` file. Starting a local webserver is required (`python3 -m http.server`)
* The user enters the string in the HTML form of the main page
* You can find this example in the tutorial: https://realpython.com/brython-python-in-browser/#the-dom-api-in-brython

### storage

* This example is an extension of the **form** project demonstrating how to use `localstorage` and save the data between page reload. It requires to start a local web server (`python3 -m http.server`).
* The data is saved as a JSON document associated with a single key of the local storage. The performance is degraded as you add more elements in the JSON file.
* This example is documented in the tutorial: https://realpython.com/brython-python-in-browser/#browser-web-api

### storage_perf

* In an attempt to overcome the performance issue of the `storage` example, this example saves each base64 encoded value into a separate key. The key is the original string entered by the user.
* This example is an extra and not described in the tutorial but is related to https://realpython.com/brython-python-in-browser/#browser-web-api

## chrome_extensions

### hello_js

* Example of a JavaScript Google Chrome extension
* In the tutorial: https://realpython.com/brython-python-in-browser/#hello-world-extension-in-js

### hello_py

* Same example as hello_js using Brython
* In the tutorial: https://realpython.com/brython-python-in-browser/#hello-world-extension-in-python

## console

* Brython console as an iframe embedded in an HTML file. Does not require to run a local web server. Opening `index.html` with a browser is sufficient to test it.
* This is an extra not described in the tutorial.
* Check out https://brython.info/console.html to see it online.

## github_install

* `index.html` loading the Brython engine from GitHub. You can open the file directly. It only displays a message box with "Hello Real Python."
* In the tutorial: https://realpython.com/brython-python-in-browser/#github-installation

## hashes

* In the same vein as the Base64 encode application, this one generates the hash, SHA-1, SHA-256 or SHA-512, of a string. It adds a dropdown to select the desired algorithm (SHA-1, SHA-256, or SHA-512).
* This serves as the basis for a translation to the same application with Vue.js (see **vuejs** project below).
* It requires a local web server.
* This is an extra not described in the tutorial, but serves the bases as the Vue.js example and you can read about it at https://realpython.com/brython-python-in-browser/#web-ui-framework

## import

* Shows how to import an external Python module. The external module is `functional.py`. The main Python code is embedded in the HTML page.
* It requires a local web server.
* Read about it in the tutorial: https://realpython.com/brython-python-in-browser/#import-in-brython

## import_js

* Expands on the `import` example by allowing the creation of `brython_module.js` generated with `brython-cli --modules`.
* This requires a Python virtual environment with Brython installed (`pip install brython`) to have `brython-cli` available in the PATH. The generated files are available in the sub-directory `dist_example`.
* You can open `dist_example/index.html` with a browser, without the need for a webserver to run locally, because the dependencies are only JS files (`brython.js` and `brython_modules.js`).
* You can read more about this approach in the tutorial at https://realpython.com/brython-python-in-browser/#reduce-import-size

## npm_install

* Example of a Brython project installed with npm. See the corresponding tutorial section for more details.
* Tutorial section: https://realpython.com/brython-python-in-browser/#npm-install

## pip_install

* Example of a Brython project installed with `pip`.
* Tutorial section: https://realpython.com/brython-python-in-browser/#pypi-install

## sha256

* Application to generate the SHA-256 hash of a given string. The data is stored as JSON in a key of the localstorage to preserve the calculations between page reloads.
* This is an extra not described in the tutorial, but serves the basis of the Vue.js example. You can read about it at https://realpython.com/brython-python-in-browser/#web-ui-framework

## vuejs

* Brython and Vue.js implementation of `hashes`. Requires a local web server to be running.
* The Vue.js example is documented at https://realpython.com/brython-python-in-browser/#web-ui-framework

## wasm

* An example demonstrating the generation of a WASM file, the loading of the file, and usage of the function from Brython. The source code of the WASM file is Rust.
* This requires you to have the Rust compiler installed on a local machine. Check the details in the Brython tutorial. A local web server is needed as it requires loading the wasm file.
* The web server can be started in the directory `wasm/op/web`. The debug wasm file is included. This is only for demonstration. The `add` function does not handle negative and big integers.
* Documented in the tutorial at https://realpython.com/brython-python-in-browser/#webassembly

## zero_install

* An example demonstrating a minimum Brython project. The Brython engine is fetched from a CDN, and the Python code is embedded on the page. No need for a local web server, no need for a local Python environment either, just a browser with JavaScript enabled :-)
* In the tutorial at https://realpython.com/brython-python-in-browser/#cdn-server-install
