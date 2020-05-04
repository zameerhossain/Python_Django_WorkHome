import sqlite3 as sq
from sqlite3 import Error

def creat_tabel(conn,table):
    c = conn.cursor()
    c.execute(table)

def insert(conn,val):
    c = conn.cursor()
    c.execute("""INSERT INTO author VALUES(?,?,?)""",val)
    conn.commit()


def start():
    author1=(1,"almasud","Abdullah Al Masud")
    author2=(2,"rimon","Rimol Ali")
    author3=(3,"niloy","Niloy Roy")
    author4=(4,"sourov","Sourov Deb Sharma")
    author5=(5,"sathi","Sathi Rani Roy")

    try:
        conn=sq.connect('01_author.sqlite')
        table=""" CREATE TABLE IF NOT EXISTS author(
                                                id integer PRIMARY KEY,
                                                username text UNIQUE,
                                                author_name text NOT NULL
                                               
                                            ); """

        creat_tabel(conn,table)

        insert(conn,author1)
        insert(conn,author2)
        insert(conn,author3)
        insert(conn,author4)
        insert(conn,author5)
        print("done")


    except Error as e:
        print(e)
    finally:
        conn.close()


def read():
    database = r"01_author.sqlite"
    try:
        conn=sq.connect(database)
        c=conn.cursor()
        c.execute("SELECT id,author_name  FROM author")
        rows=c.fetchall()
        for id,a_name in rows:
            print("{}-{}".format(id,a_name))




    except Error as e:
        print("no database found")

if __name__ == '__main__':
    start()
    read()