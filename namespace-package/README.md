# What's a Namespace Package?

Materials for the corresponding Real Python article.

You have the Hello World example, and the source code for the Snake Shop Corporation example that's hosted on PyPI. Aditionally, as an extra, you have the code to generate the fake data used.

You need to install every subpackage to get it working properly.

## Examples

In this repository you'll find four different examples showing ways namespace packages work or can be used.

### Hello World

A basic structure to illustrate namespace packages at their most basic.

### Business

A typical use case of namespace packages is for large businesses that want to make sure all their code is packaged under a namespace. In this and subsequent examples, you take the fictional Snake Corporation.

For this example the Snake Corporation has two separate utility packages, but when both are installed, both are available under the same `snake_corp` namespace:

```py
>>> from snake_corp import dateutil
>>> from snake_corp import magic
```

### Distributed Data Repository

In this example, you make a namespace package that serves as a wrapper around your data files. This allows you to create separate packages that only contain data.

This way, an organization like Real Python can have some core functionality in the main package, like the functions to read the data, and then have many satellite data packages, that just include a particular dataset and inserts it into the namespace so it can be read by the core package.

### Plugin System

In this example you take the data repository example further, and add a plugin system for the readers. So you can support your own custom formats. 