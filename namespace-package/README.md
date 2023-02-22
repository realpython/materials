# What's a Python Namespace Package, and What's It For?

Materials for the corresponding Real Python tutorial, [What's a Python Namespace Package, and What's It For?](https://realpython.com/python-namespace-package/).

You have the source code for the Snake Corporation example that's hosted on PyPI. Aditionally, as an extra, you have the code to generate the fake data used.

You need to install every subpackage to get the code working properly.

## Examples

In this repository, you'll find three different examples showing ways that namespace packages work or can be used.

### Business

A typical use case of namespace packages is for large businesses that want to make sure all their code is packaged under a namespace. In this and subsequent examples, you play the role of the fictional Snake Corporation.

For this example, the Snake Corporation has two separate utility packages, but when both are installed, both are available under the same `snake_corp` namespace:

```py
>>> from snake_corp import dateutil
>>> from snake_corp import magic
```

### Distributed Data Repository

In this example, you make a namespace package that serves as a wrapper around your data files. This allows you to create separate packages that only contain data.

This way, an organization like Real Python can have some core functionality in the main package, like the functions to read the data, and then have many satellite data packages that just include a particular dataset and insert it into the namespace so it can be read by the core package.

### Plugin System

In this example, you take the data repository example further by adding a plugin system for the readers so that you can support your own custom formats. 
