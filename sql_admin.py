import sqlite3
from sqlite3 import Error


def create_connection(path):
    """ 
        create a connection with the sqlite database
        conn: path
    """
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(e)

    return connection

def create_table(conn, create_table_sql):
    """ 
        create a table from the create_table_sql statement
        conn: Connection object
        create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(f"Error creating table {e}")

# usage
# author = ("hahahaha")
# insert_author(connection, author)
def insert_author(conn, author):
    sql = ''' 
        INSERT INTO author_tracker(author)
        VALUES(?)
    '''
    cur = conn.cursor()
    cur.execute(sql, (author,))
    conn.commit()

# usage
# word = ("hihihi")
# insert_word(connection, word)
def insert_word(conn, word):
    sql = ''' 
        INSERT INTO word_tracker(word)
        VALUES(?)
    '''
    cur = conn.cursor()
    cur.execute(sql, (word,))
    conn.commit()

# usage
# update_authors(connection, "w")

def update_authors(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM author_tracker")
    rows = cur.fetchall()

    for row in rows:
        if row[0] == query:
            tempIncrement = row[1] + 1
            # We have found it and want to update
            sql = ''' UPDATE author_tracker
                SET count = ?
                WHERE author = ?
            '''
            cur = conn.cursor()
            cur.execute(sql, (tempIncrement, query))
            conn.commit()
            return
    
    # Otherwise it is not there and we create it.
    insert_author(conn, query)
    
    
# usage
# update_words(connection, "hiii!") 
def update_words(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM word_tracker")

    rows = cur.fetchall()
    for row in rows:
        if row[0] == query:
            tempIncrement = row[1] + 1
            # We have found it and want to update
            sql = ''' UPDATE word_tracker
                SET count = ?
                WHERE word = ?
            '''
            cur = conn.cursor()
            cur.execute(sql, (tempIncrement, query))
            conn.commit()
            return
    
    # Otherwise it is not there and we create it.
    insert_word(conn, query)

def select_stats(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM author_tracker")
    rows = cur.fetchall()
    return rows

def select_words(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM word_tracker")
    rows = cur.fetchall()
    return rows

sql_create_word_tracker = """ 
    CREATE TABLE IF NOT EXISTS word_tracker (
        word TEXT NOT NULL,
        count integer DEFAULT 1
    );
"""

sql_create_author_tracker = '''
    CREATE TABLE IF NOT EXISTS author_tracker (
        author TEXT NOT NULL,
        count INTEGER DEFAULT 1
    );
'''

connection = create_connection("pythonsqlite.db")

create_table(connection, sql_create_word_tracker)
create_table(connection, sql_create_author_tracker)