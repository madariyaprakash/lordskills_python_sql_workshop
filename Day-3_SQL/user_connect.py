from mysql_connect import  mysql_connect

def all_users():
    conn = mysql_connect()
    cursor = conn.cursor()
    query = "select * from user;"
    cursor.execute(query)
    data = cursor.fetchall()
    # using zip we can map the key and value
    columns = [c[0] for c in cursor.description]
    # print(columns)
    dict_data = [dict(zip(columns,d)) for d in data]
    return dict_data

def fetch_one_record(id):
    conn = mysql_connect()
    cursor = conn.cursor()
    query = f"select * from user where user_id = {id};"
    cursor.execute(query)
    data = cursor.fetchone()
    return data


def add_user(first_name, last_name, email):
    conn = mysql_connect()
    cursor = conn.cursor()
    query = f"insert into user (first_name, last_name, email) values ('{first_name}', '{last_name}','{email}');"
    cursor.execute(query)
    conn.commit()
    print("record added", cursor.rowcount) # should be 1 if inserted


def update_user(id, first_name):
    conn = mysql_connect()
    cursor = conn.cursor()
    query = f"update user set first_name = '{first_name}' where user_id = {id};"
    cursor.execute(query)
    conn.commit()
    print("record updated")

def delete_user(id):
    with mysql_connect() as conn:
        with conn.cursor() as cursor:
            query = f"delete from user where user_id = {id};"
            cursor.execute(query)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"record deleted with {id}")
            else:
                print(f"There is no record with {id}")


def get_user_with_gmails():
    conn = mysql_connect()
    cursor = conn.cursor()
    query = "select * from gmail_users;"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

# print(all_users())
# print(fetch_one_record(5))
#print(add_user("priya","rajput","priya@gmail.com"))
# print(update_user(14, "Rani"))
# print(delete_user(5))
print(get_user_with_gmails())




