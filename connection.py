import mysql.connector


def setup_connection():
    con = mysql.connector.connect(
        host="localhost", user="root", password="password", database="bankDB"
    )
    return con


def search(query):
    con = setup_connection()

    cursor = con.cursor()
    cursor.execute(query)

    resultset = cursor.fetchall()

    cursor.close()
    con.close()

    return resultset


def iud(query):
    con = setup_connection()

    cursor = con.cursor()
    cursor.execute(query)

    con.commit()

    cursor.close()
    con.close()
