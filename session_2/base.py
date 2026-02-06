import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()
    menu(db)

def menu(db):
    input("Press enter to run query: ")
    query_runner(db)

def query_runner(db):
    query='''SELECT category, sum(price) as price FROM products
    GROUP BY category;'''

    result=pd.read_sql_query(query, db)
    result.plot.pie(y='price', labels=result['category'], autopct='%1.1f%%', legend=False)
    plt.ylabel('')  # Remove the y-axis label
    plt.savefig("result.png")

if __name__=="__main__":
    main()
