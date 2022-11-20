import sqlite3
from sqlite3 import Error
from data_base import sql_query


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('botDB.db')
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn: sqlite3.Connection, sql_query = sql_query.CREATE_TABLE):
    try:
        c = conn.cursor()
        c.execute(sql_query)
        conn.commit()
        print("wse ok")
    except Error as e:
        print(e)



def select_from(conn: sqlite3.Connection, sql_query: str, param: None):
    try:
        if param != None:
            c = conn.cursor()
            c.execute(sql_query, param)
            return c.fetchall()
        else:
            c = conn.cursor()
            c.execute(sql_query)
            return c.fetchall()
    except Error as e:
        print(e)


def insert_into(conn: sqlite3.Connection, sql_query: str, param: list):
    try:
        c = conn.cursor()
        c.execute(sql_query, param)
        conn.commit()
    except Error as e:
        print(e)


def update_set(conn: sqlite3.Connection, sql_query: str):
    try:
        c = conn.cursor()
        c.execute(sql_query)
        conn.commit()
    except Error as e:
        print(e)
