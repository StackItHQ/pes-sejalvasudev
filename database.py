import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sejal123',
        database='sheets_sync'
    )
    return connection

def create_data(values):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO data (name, age, university, course) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def read_all_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM data"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_data(id, values):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE data SET name = %s, age = %s, university = %s, course = %s WHERE id = %s"
    cursor.execute(query, (*values, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_data(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM data WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
