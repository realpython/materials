# Build Files Used By The Examples

The code in this directory builds the various data files used
by the example programs. There is one build program:

* build_author_book_publisher_sqlite.py

## Build the Author / Book / Publisher Database File

The build_author_book_publisher_sqlite.py file builds
a database from the `data/author_book_publisher.csv` file.
This database contains the rows of comma delimited text to describe
the data and the relationships between the data necessary
for the examples.

## Directory Structure

The directory structure is set up in such a way the
build programs (as well as the examples) can find the
data files needed for each one.

## Executing the Programs

Follow these steps to build the `data/author_book_publisher.db` database file.

* Activate your Python virtualenv
* cd into the build/code directory
* python build_author_book_publisher_sqlite.py - builds the author_book_publisher.db database file
  
  
  
 
 