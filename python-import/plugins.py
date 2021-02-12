# plugins.py

import functools
import importlib
from collections import namedtuple
from importlib import resources

# Basic structure for storing information about one plugin
Plugin = namedtuple("Plugin", ("name", "func"))

# Dictionary with information about all registered plugins
_PLUGINS = {}


def register(func):
    """Decorator for registering a new plugin"""
    package, _, plugin = func.__module__.rpartition(".")
    pkg_info = _PLUGINS.setdefault(package, {})
    pkg_info[plugin] = Plugin(name=plugin, func=func)
    return func


def names(package):
    """List all plugins in one package"""
    _import_all(package)
    return sorted(_PLUGINS[package])


def get(package, plugin):
    """Get a given plugin"""
    _import(package, plugin)
    return _PLUGINS[package][plugin].func


def call(package, plugin, *args, **kwargs):
    """Call the given plugin"""
    plugin_func = get(package, plugin)
    return plugin_func(*args, **kwargs)


def _import(package, plugin):
    """Import the given plugin file from a package"""
    importlib.import_module(f"{package}.{plugin}")


def _import_all(package):
    """Import all plugins in a package"""
    files = resources.contents(package)
    plugins = [f[:-3] for f in files if f.endswith(".py") and f[0] != "_"]
    for plugin in plugins:
        _import(package, plugin)


def names_factory(package):
    """Create a names() function for one package"""
    return functools.partial(names, package)


def get_factory(package):
    """Create a get() function for one package"""
    return functools.partial(get, package)


def call_factory(package):
    """Create a call() function for one package"""
    return functools.partial(call, package)
