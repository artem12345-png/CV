import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect(
    user='postgres',
    password='****',
    host='127.0.0.1.',
    port='5432'
)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = con.cursor()
sql_create_db = 'create database test2'
cursor.execute(sql_create_db)

con = psycopg2.connect(
    dbname='test2',
    user='postgres',
    password='****',
    host='127.0.0.1.',
    port='5432'
)
cursor.execute("create table users (id serial primary key, login varchar(64), password varchar(64))")

cursor.execute("INSERT INTO users (login, password) VALUES (%s, %s)", ("afiskon", "123"))
cursor.execute("INSERT INTO users (login, password) VALUES (%s, %s)", ("eax", "456"))

cursor.execute("SELECT id, login, password FROM users")
print(cursor.fetchall())

con.commit()
cursor.close()
con.close()

print(con)
