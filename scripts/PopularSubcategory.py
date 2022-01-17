import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
import matplotlib.pyplot as plt
import seaborn as sns

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

def lastmonth_popular_subcategory(dbName:str,start_date:str,last_date : str):
    """
    Parameters
    ----------
    dbName :
        str:
    start_date :
        str:
    last_date :
        str:
    dbName :
        str:
    start_date :
        str:
    last_date :
        str:
    dbName:str :
    start_date:str :
    last_date:str :
    Returns
    -------
    """
    conn, cur = DBConnect(dbName)


    sqlquery = f"SELECT sc.subcategory_name , COUNT(vc.idsubcat) AS popular FROM vidcat AS vc INNER JOIN subcategory AS sc ON sc.idsubcat = vc.idsubcat WHERE vc.idvideo IN (SELECT idvideo FROM video WHERE publish_date BETWEEN '{start_date}' AND '{last_date}') GROUP BY sc.subcategory_name ORDER BY popular DESC"
    #res = cur.execute(sqlquery)
    data = pd.read_sql(sqlquery,conn)
    print(data)
   

    conn.commit()
    cur.close()

    return 


if __name__ == "__main__":
    lastmonth_popular_subcategory(dbName='pandavideo',start_date='2022-5-1',last_date='2022-5-31')
    