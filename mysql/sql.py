import pymysql

e=pymysql.connect(
    host="localhost",
    user='root',
    passwd="Ah$$2825",
    db="news",
    charset="utf8"
)

c = e.cursor()

c.execute("SELECT * FROM `news`")
r = c.fetchall()
print(r)
e.commit

c.execute("INSERT INTO `news`(`title`,`source`,`date`,`url`,`description`)"+
            "VALUES(%(a)s,%(b)s,%(c)s,%(d)s,%(e)s)"
            , {
                "c": input("date:"),
                "a": input("title:"),
                "b": input("source:"),
                "e": input("description:"),
                "d": input("url:")
            })
e.commit()

c.execute(
            "DELETE FROM `news` WHERE `id`=%s"
            , [
                input("id:")
            ])
e.commit()

e.close()
