from test_mysql_connector import create_connection

def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    query = "select * from user;"
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [c[0] for c in cursor.description]

    # using zip() function map the user coulmns with corresponding data
    final_result = [dict(zip(columns, row)) for row in result]

    # print(columns)
    print(final_result)


def get_user_on_id(id):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"select * from user where user_id = {id}"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)


def add_new_user(first_name, last_name, email):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"insert into user (first_name, last_name, email) values ('{first_name}','{last_name}','{email}');"
    cursor.execute(query)
    conn.commit()
    if cursor.rowcount > 0:
        print("record inserted")
    else:
        print("error occured")

def update_user(first_name, last_name, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"update user set first_name='{first_name}', last_name='{last_name}' where user_id={user_id};"
    cursor.execute(query)
    conn.commit()
    if cursor.rowcount > 0:
        print("record updated")
    else:
        print("error occured")

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"delete from user where user_id={user_id}"
    cursor.execute(query)
    conn.commit()
    if cursor.rowcount >0:
        print("record deleted")
    else:
        print("error occured")


# print(get_all_users())
# print(get_user_on_id(2))
#print(add_new_user("new","user","new@gmail.com"))
# print(update_user("abc","user",2))
print(delete_user(2))

