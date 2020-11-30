from browser import document, window

double_first_and_add = None


def add_rust_fn(module):
    global double_first_and_add
    double_first_and_add = module.instance.exports.double_first_and_add


def add_numbers(evt):
    nb1 = document["number-1"].value or 0
    nb2 = document["number-2"].value or 0
    res = double_first_and_add(nb1, nb2)
    document["result"].innerHTML = f"Result: ({nb1} * 2) + {nb2} = {res}"


document["submit"].bind("click", add_numbers)
window.WebAssembly.instantiateStreaming(window.fetch("op.wasm")).then(
    add_rust_fn
)
