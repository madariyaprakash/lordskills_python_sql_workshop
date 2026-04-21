import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password="Prakash@000",
        database="lk_db"
    )
    return conn

def create_new_table():
    conn = create_connection()
    cursor = conn.cursor()
    query = """
        create table user_test (
            user_id int primary key auto_increment,
            first_name varchar(50),
            last_name varchar(50),
            email varchar(100) unique,
            created_at timestamp default current_timestamp
        );
    """
    cursor.execute(query)
    conn.commit()
    print("table created")

# conn = create_connection()
# if conn.is_connected():
#     print("Connection successful!")
# else:
#     print("Connection failed.")

print(create_new_table())