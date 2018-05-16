# import pymysql
import pyodbc


def create_database(database_path: str):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=WordsDB;'
                          'Trusted_Connection=Yes')
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "create table words(word varchar(25) primary key not null, usage_count int not null default 1);"
        cur.execute(ddl)

    print(database_path)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=WordsDB;'
                          'Trusted_Connection=Yes')
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check if word is in there #
            sql = "select count(word) from words where word='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word='" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cur.execute(sql)
        print("Database save complete!")

    print(database_path)
    conn.close()
