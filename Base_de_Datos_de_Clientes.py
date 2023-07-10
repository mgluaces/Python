import mysql.connector

def create_db_connection():
    connection = mysql.connector.connect(host='localhost:3306',
                                         database='clientes',
                                         user='root', 
                                         password='TxIkY0017$')
    return connection

def get_all_clients():
    connection = create_db_connection()
    cursor = connection.cursor()  
    cursor.execute('SELECT * FROM clientes')
    clients = cursor.fetchall()
    connection.close()
    return clients

def add_client(nombre, apellido, email):  
    connection = create_db_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO clientes (nombre, apellido, email) VALUES (%s, %s, %s)"
    val = (nombre, apellido, email)
    cursor.execute(sql, val)
    connection.commit()
    connection.close()
    
'''
Este código Python define funciones para conectarse a una base de datos MySQL de clientes, recuperar todos los clientes 
y agregar un nuevo cliente. Utiliza la biblioteca mysql.connector para conectarse a la base de datos y realizar consultas SQL.
'''
