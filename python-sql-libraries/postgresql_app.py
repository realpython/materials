import psycopg2
from psycopg2 import OperationalError

# Change these connection parameters to match your PostgreSQL server:
DB_USER = "postgres"
DB_PASSWORD = "abc123"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    # Connecting to the default database and creating sm_app
    connection = create_connection(
        "postgres", DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
    )

    create_database_query = "CREATE DATABASE sm_app"
    create_database(connection, create_database_query)

    connection = create_connection(
        "sm_app", DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
    )

    # Creating tables
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT,
      nationality TEXT
    )
    """

    execute_query(connection, create_users_table)

    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
      id SERIAL PRIMARY KEY,
      title TEXT NOT NULL,
      description TEXT NOT NULL,
      user_id INTEGER REFERENCES users(id)
    )
    """

    execute_query(connection, create_posts_table)

    # Not shown in the tutorial: the comments and likes tables
    create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
      id SERIAL PRIMARY KEY,
      text TEXT NOT NULL,
      user_id INTEGER REFERENCES users(id),
      post_id INTEGER REFERENCES posts(id)
    )
    """

    create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
      id SERIAL PRIMARY KEY,
      user_id INTEGER REFERENCES users(id),
      post_id INTEGER REFERENCES posts(id)
    )
    """

    execute_query(connection, create_comments_table)
    execute_query(connection, create_likes_table)

    # Inserting records
    users = [
        ("James", 25, "male", "USA"),
        ("Leila", 32, "female", "France"),
        ("Brigitte", 35, "female", "England"),
        ("Mike", 40, "male", "Denmark"),
        ("Elizabeth", 21, "female", "Canada"),
    ]

    user_records = ", ".join(["%s"] * len(users))

    insert_query = f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, users)

    posts = [
        ("Happy", "I am feeling very happy today", 1),
        ("Hot Weather", "The weather is very hot today", 2),
        ("Help", "I need some help with my work", 2),
        ("Great News", "I am getting married", 1),
        ("Interesting Game", "It was a fantastic game of tennis", 5),
        ("Party", "Anyone up for a late-night party today?", 3),
    ]

    post_records = ", ".join(["%s"] * len(posts))

    insert_query = f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, posts)

    # Not shown in the tutorial: the comments and likes records
    comments = [
        ("Count me in", 1, 6),
        ("What sort of help?", 5, 3),
        ("Congrats buddy", 2, 4),
        ("I was rooting for Nadal though", 4, 5),
        ("Help with your thesis?", 2, 3),
        ("Many congratulations", 5, 4),
    ]

    comment_records = ", ".join(["%s"] * len(comments))

    insert_query = f"INSERT INTO comments (text, user_id, post_id) VALUES {comment_records}"

    cursor.execute(insert_query, comments)

    likes = [(1, 6), (2, 3), (1, 5), (5, 4), (2, 4), (4, 2), (3, 6)]

    like_records = ", ".join(["%s"] * len(likes))

    insert_query = (
        f"INSERT INTO likes (user_id, post_id) VALUES {like_records}"
    )

    cursor.execute(insert_query, likes)

    # Selecting records
    select_users = "SELECT * FROM users"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)

    # Updating table records
    update_post_description = """
    UPDATE
      posts
    SET
      description = 'The weather has become pleasant now'
    WHERE
      id = 2
    """

    execute_query(connection, update_post_description)

    select_post_description = "SELECT description FROM posts WHERE id = 2"

    post_description = execute_read_query(connection, select_post_description)

    for description in post_description:
        print(description)

    # Deleting table records
    delete_comment = "DELETE FROM comments WHERE id = 2"
    execute_query(connection, delete_comment)
