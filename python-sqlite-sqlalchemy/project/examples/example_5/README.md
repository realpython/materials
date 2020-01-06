# Example 5

This example uses Sqlite and SQL queries to access the
author_book_publisher.db database file to
get data into the program and run various python functions
on it.

The database captures the relationships between tables, and 
this is used to generate interesting data about the database. 
However, the original CSV file is essentially re-created in 
the *get_authors()* function in order to create the authors
hierarchical data necessary to generate the tree view 
presented by the main program. 
