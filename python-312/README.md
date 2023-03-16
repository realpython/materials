# Python 3.12 Demos

This repository holds example code that demos some of the new features in Python 3.12.

## Introduction

You need Python 3.12 installed to run these examples. See the following tutorial instructions:

- [How Can You Install a Pre-Release Version of Python](https://realpython.com/python-pre-release/)

You can learn more about Python 3.12's new features in the following Real Python tutorials:

- [Python 3.12 Preview: Ever Better Error Messages](https://realpython.com/python312-error-messages/)

You'll find examples from all these tutorials in this repository.

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### Improved Error Messages

Run [`encoder.py](encoder.py) to create an encoded message like the one shown in the tutorial. You can decode the message using [`decoder.py](decoder.py).

You can swap the import statement to `import d from this` in either of the files to encounter the improved error message:

```python
>>> import d from this
  File "<stdin>", line 1
    import d from this
    ^^^^^^^^^^^^^^^^^^
SyntaxError: Did you mean to use 'from ... import ...' instead?
```

In [`local_self.py`](local_self.py), you can see a naive reproduction of another improved error message. Pick apart the example code to learn more about how this was implemented in Python 3.12. 

See [Ever Better Error Messages in Python 3.12](https://realpython.com/python312-error-messages/) for more information.

## Authors

- **Martin Breuss**, E-mail: [martin@realpython.com](martin@realpython.com)
- **Bartosz Zaczyński**, E-mail: [bartosz@realpython.com](bartosz@realpython.com)
- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
