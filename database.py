# database.py
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
    cursor.executemany("INSERT INTO data (name, age, university, course) VALUES (%s, %s, %s, %s)", values)
    connection.commit()
    cursor.close()
    connection.close()

def read_all_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_data(id, values):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE data SET name=%s, age=%s, university=%s, course=%s WHERE id=%s", (*values, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_data(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
