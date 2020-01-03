# Build Files Used By The Examples

The code in this directory builds the various data files used
by the example programs. There are three build programs:

 * build_temp_data_csv.py
 * build_temp_data_sqlite.py
 * build_author_book_publisher_sqlite.py
 
## Build the Temperature CSV File
 
 The build_temp_data_csv.py file builds a CSV data file
 (temp_data.csv) in the data directory
 containing temperature samples taken by students in a class.
 The top row contains the labels, the students name followed
 by a date value for each Wednesday of the week for a year.
 
 It then creates data for each sample based on a table of 
 temperature data, +/- 10 to make the data look variable
 and reasonable.
 
## Build the Temperature Database File
 
 The build_temp_data_sqlite.py file builds a Sqlite database
 from the previously created temp_data.csv file called 
 temp_data.db in the data directory. 
 
## Build the Author / Book / Publisher Database File
 
 The build_author_book_publisher_sqlite.py file builds
 a database from the data/author_book_publisher.csv file.
 This database contains the tables necessary to describe 
 the data and the relationships between the data necessary
 for the examples.
 
## Directory Structure
 
 The directory structure is set up in such a way the
 build programs (as well as the examples) can find the
 data files needed for each one.
 
## Executing the Programs
 
  * Activate your Python virtualenv
  * cd into the build/code directory
  * python build_temp_data_csv.py - builds the csv data file
  * python build_temp_data_sqlite.py - builds the temperature data from the csv file
  * python build_author_book_publisher_sqlite.py - builds the author_book_publisher.db database file
  
  
  
 
 