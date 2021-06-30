import pymysql
from random import random as rand

db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="bookshare",
    charset="utf8"
)

cursor=db.cursor()
def create_database():
    cursor.execute(
        "create table user("
        "   userid char(10) default null,"
        "   username varchar(20) default null,"
        "   sex varchar(6) default null,"
        "   age smallint default null,"
        "   password varchar(64) default null"
        ");"
    )
    cursor.execute(
        "create table recm_book("
        "   userid char(10) default null,"
        "   bookid char(10) default null"
        ");"
    )
    cursor.execute(
        "create table book("
        "   bookid char(10) default null,"
        "   bookname varchar(20) default null,"
        "   bookinfo varchar(150) default null"
        ");"
    )
    cursor.execute(
        "create table comment("
        "   userid char(10) default null,"
        "   bookid char(10) default null,"
        "   cmid char(10) default null,"
        "   info varchar(150) default null"
        ");"
    )
    db.commit()
    return
create_database()
cursor.close()
db.close()