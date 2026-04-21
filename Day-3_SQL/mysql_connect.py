import mysql.connector
import sqlite3

# create database
def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prakash@000"
    )
    cursor = conn.cursor()
    query = "Create database if not exists nice_db;"
    cursor.execute(query)
    print("database created")

def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prakash@000",
        database="nice_db"
    )
    cursor = conn.cursor()
    query = """
                create table user (
                user_id int primary key auto_increment,
                first_name varchar(50),
                last_name varchar(50),
                email varchar(150) unique,
                created_at timestamp default current_timestamp
            );
        """
    cursor.execute(query)
    conn.commit()
    print("user table created")

# establish connection
def mysql_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prakash@000",
        database="user_db"
    )
    return conn

# if conn.is_connected():
#     print("connection established")



# ========== for sqlite3===========================
def sqlite_connect():
    return sqlite3.connect("test_db.sqlite")


def create_sqlite_user_table():
    conn = sqlite_connect()
    cursor = conn.cursor()
    query = """
                create table user (
                user_id int primary key,
                first_name varchar(50),
                last_name varchar(50),
                email varchar(150) unique,
                created_at timestamp default current_timestamp
            );
        """
    cursor.execute(query)
    conn.commit()
    print("user table created")

# print(create_database())
# print(create_sqlite_user_table())



