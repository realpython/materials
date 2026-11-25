# Creating and Modifying PDFs With Python

This folder contains resources and materials for Real Python's [Creating and Modifying PDFs With Python](https://realpython.com/creating-modifying-pdf/) tutorial.

There are two subfolders in this folder:

1. **`practice_files/`:** Contains the sample PDFs used in the tutorial
2. **`source_code/`:** Contains source code from the tutorial

The source code files are organized by section of the tutorial, and the start of each subsection is indicated with comments.

## Requirements

The code requires Python 3.11 or later. Install the pinned versions of `pypdf` and ReportLab that the tutorial uses with:

```sh
$ python -m pip install -r requirements.txt
```

The tutorial pins `pypdf` to 3.8.1 because the concatenating and merging examples use the `PdfMerger` class, which later `pypdf` releases removed.

The content of the companion tutorial was adapted from the "Creating and Modifying PDF Files" chapter of the book [*Python Basics: A Practical Introduction to Python 3*](https://realpython.com/products/python-basics-book/). If you enjoy this tutorial, check out the full book!
