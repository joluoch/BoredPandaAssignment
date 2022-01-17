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

    return data

def plot_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()

if __name__ == "__main__":
    data = lastmonth_popular_subcategory(dbName='pandavideo',start_date='2022-1-1',last_date='2022-1-31')
    plot_bar(data, 'subcategory_name','popular','plot showing last months popular subcategory','subcategory','poplarity count')