# Python Modules and Packages – An Introduction

This folder provides the code examples for the Real Python tutorial [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/).

## Setup

The examples use only the standard library, so there's nothing to install. They were tested on Python 3.14, which is the version the tutorial's output reflects. On older versions, some output differs. For example, `dir()` lists `'__annotations__'` before Python 3.14, and a namespace package's repr omits its `from [...]` path list before Python 3.12.

## Usage

The tutorial changes `mod.py`, `pkg/__init__.py`, and `pkg/mod1.py` as it goes, so each stage lives in its own folder:

| Folder | Section | Contents |
| --- | --- | --- |
| `module_basics/` | Python Modules: Overview | `mod.py`, which only defines objects |
| `module_as_script/` | Executing a Module as a Script | `mod.py`, which prints output every time it runs |
| `main_guard/` | Executing a Module as a Script | `mod.py` and `fact.py`, which check `__name__` |
| `module_reload/` | Reloading a Module | `mod.py`, which prints when it's loaded |
| `package_basics/` | Python Packages | `pkg/` with `mod1.py` and `mod2.py` and no `__init__.py` |
| `package_init_data/` | Package Initialization | `pkg/__init__.py` defining the package-level list `A` |
| `package_init_imports/` | Package Initialization | `pkg/__init__.py` importing `mod1` and `mod2` |
| `import_star/` | Importing `*` From a Package | `pkg/` with four modules and no `__init__.py` |
| `import_star_all/` | Importing `*` From a Package | `pkg/` with `__all__` in `__init__.py` and `mod1.py` |
| `subpackages_absolute/` | Subpackages | `pkg/sub_pkg1/` and `pkg/sub_pkg2/`, with `mod3.py` using an absolute import |
| `subpackages_relative/` | Subpackages | The same tree, with `mod3.py` using relative imports |

Change into a folder before you start the interpreter, so that `mod` or `pkg` is importable from the current directory. For example:

```console
$ cd main_guard/
$ python mod.py
Executing as standalone script
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x7f1ddeba0c20>

$ python fact.py 6
720
```

```console
$ cd subpackages_relative/
$ python
>>> from pkg.sub_pkg2 import mod3
<module 'pkg.sub_pkg1' (namespace) from ['.../subpackages_relative/pkg/sub_pkg1']>
[mod1] foo()
```

Start a fresh interpreter session for each example. Python loads a module only once per session, and a submodule that you've already imported shows up in the output of `from pkg import *`.

The code is formatted to the repository's style, so it differs slightly from the tutorial. It uses double quotes, and the `if __name__ == "__main__":` lines don't have parentheses. Some import lines carry `# noqa` comments, because they deliberately show patterns that a linter flags:

- `package_init_imports/pkg/__init__.py` imports two modules on one line after a `print()` call.
- `mod3.py` in both `subpackages_*/` folders imports at the bottom of the file, after the definitions.
