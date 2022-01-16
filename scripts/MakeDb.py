import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    """
    Parameters
    ----------
    dbName :
        Default value = None)
    Returns
    -------
    """
    conn = mysql.connect(host='localhost', user='root',password = 'root1234',database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    """
    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :
    Returns
    -------
    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    """
    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :
    Returns
    -------
    """
    conn, cur = DBConnect(dbName)
    sqlFile = '../schema/schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
            print("Tables created Successfully")
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return


def insert(dbName: str) -> None:
    """
    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :
    Returns
    -------
    """
    conn, cur = DBConnect(dbName)
    sqlFile = '../schema/insertstatment.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
            print("Data Inserted Successfully")
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return    

if __name__ == "__main__":
    createDB(dbName='pandavideo')
    createTables(dbName='pandavideo')
    insert(dbName='pandavideo')