# Introduction to Python SQL Libraries

This folder provides the code examples for the Real Python tutorial [Introduction to Python SQL Libraries](https://realpython.com/python-sql-libraries/).

Each script builds the same small social media database, `sm_app`, with `users`, `posts`, `comments`, and `likes` tables, and then runs the tutorial's `CREATE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE` queries against it:

- `sqlite_app.py`: Uses the standard-library `sqlite3` module to work with an SQLite database file, `sm_app.sqlite`.
- `mysql_app.py`: Uses `mysql-connector-python` to create and work with the `sm_app` database on a MySQL (or MariaDB) server.
- `postgresql_app.py`: Uses `psycopg2` to create and work with the `sm_app` database on a PostgreSQL server.

The helper functions, such as `create_connection()`, `execute_query()`, and `execute_read_query()`, are importable from each module. The tutorial's queries run when you execute a file as a script.

## Requirements

The code needs Python 3.10 or later, as required by the pinned versions of the third-party drivers. The SQLite example uses only the standard library and runs on any Python 3.6+.

## Installation

The MySQL and PostgreSQL examples need third-party drivers:

```console
$ python -m pip install -r requirements.txt
```

## Usage

### SQLite

No server is needed. Run the script, and it creates `sm_app.sqlite` in the current working directory:

```console
$ python sqlite_app.py
Connection to SQLite DB successful
Query executed successfully
...
(1, 'James', 25, 'male', 'USA')
(2, 'Leila', 32, 'female', 'France')
...
['post', 'comment', 'name']
...
('The weather is very hot today',)
Query executed successfully
('The weather has become pleasant now',)
Query executed successfully
```

Delete `sm_app.sqlite` before running the script again, or the records are inserted a second time.

### MySQL

You need a running MySQL or MariaDB server. The script connects as `root` with an empty password on `localhost`. To use other credentials, edit the `HOST_NAME`, `USER_NAME`, and `USER_PASSWORD` constants at the top of `mysql_app.py`.

For example, on Ubuntu, you can install and start a MariaDB server and allow `root` to log in with an empty password like this:

```console
$ sudo apt update && sudo apt install -y mariadb-server
$ sudo service mariadb start
$ sudo mariadb -e "ALTER USER root@localhost IDENTIFIED VIA mysql_native_password USING PASSWORD('') OR unix_socket; FLUSH PRIVILEGES;"
```

Then run the script, which creates the `sm_app` database itself:

```console
$ python mysql_app.py
Connection to MySQL DB successful
Database created successfully
Connection to MySQL DB successful
Query executed successfully
...
```

To start over, drop the database with `sudo mariadb -e "DROP DATABASE sm_app"`.

### PostgreSQL

You need a running PostgreSQL server. The script connects as the `postgres` user with the password `abc123` on `127.0.0.1:5432`. To use other credentials, edit the `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` constants at the top of `postgresql_app.py`.

For example, on Ubuntu, you can install and start a PostgreSQL server and set the password like this:

```console
$ sudo apt update && sudo apt install -y postgresql
$ sudo service postgresql start
$ sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'abc123';"
```

Then run the script, which creates the `sm_app` database itself:

```console
$ python postgresql_app.py
Connection to PostgreSQL DB successful
Query executed successfully
Connection to PostgreSQL DB successful
Query executed successfully
...
(1, 'James', 25, 'male', 'USA')
...
('The weather has become pleasant now',)
Query executed successfully
```

If `sm_app` already exists, the script reports the error and carries on, so the records are inserted a second time. To start over, drop the database with `sudo -u postgres psql -c "DROP DATABASE sm_app"`.
