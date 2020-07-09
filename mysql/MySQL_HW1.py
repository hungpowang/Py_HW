import pymysql
import prettytable
import sql_config

e = pymysql.connect(**sql_config.config)

c = e.cursor()


def show_table(conn, cur, table_name):
    '''
    以表格方式印出資料表
    '''
    # 取得table所有列
    cur.execute("SELECT * FROM `" + table_name + "`")
    rows = cur.fetchall()
    conn.commit
    # 取得table所有欄位名稱
    cur.execute("SHOW COLUMNS FROM `" + table_name + "`")
    col_info = cur.fetchall()
    conn.commit
    col_names = []
    for c in col_info:
        col_names.append(c[0]) 
    # 用prettytable印出來
    table = prettytable.PrettyTable(col_names, encoding='utf8')
    for r in rows:
        table.add_row(list(r))
    print("TABLE:", table_name)
    print(table)
# show_table(e, c, "members")


def insert_data(conn, cur, table_name):
    '''
    使用者輸入新增資料
    '''
    # # 基本新增方式
    # c.execute("INSERT INTO `members`(`name`,`birthday`,`address`) VALUES('Jason', '1963-07-31', 'LA')")
    # conn.commit()
    # # 以字典帶入的新增方式
    # c.execute("INSERT INTO `members`(`name`,`birthday`,`address`) VALUES(%(a)s,%(b)s,%(c)s)",
    # 	    { "b":"2048-06-28", "a":"Rachal", "c":"NYC" })
    # conn.commit()
    #  以使用者輸入至字典帶入的新增方式
    cur.execute("INSERT INTO `members`(`name`,`birthday`,`address`) VALUES(%(a)s,%(b)s,%(c)s)",
            {
            "a": input("name: "),
            "b": input("Birthday: "),
            "c": input("address: ")
            })
    conn.commit()
# insert_data(e, c, "members")


def delete_data(conn, cur, table_name):
    '''
    詢問id式刪除資料
    '''
    cur.execute("DELETE FROM `members` WHERE `id`=%s", [ input("id: ") ])
    conn.commit()

# delete_data(e, c, "members")


# def update_data(conn, cur, table_name):
#     '''
#     修改資料：詢問(欄位,id,value)
#     '''
#     print("update data by (column, value, id) ...")
#     # cur.execute("UPDATE `members` SET `%(col_name)s`='%(value)s' WHERE `id`=%(data_id)s" ,
#     cur.execute("UPDATE `members` SET `name`='Shawn' WHERE `id`=%(data_id)s" ,
#             {
#             # "col_name":'name',
#             # "value":"Shawn",
#             "data_id": "18"
#             })
#     conn.commit()
# update_data(e, c, "members")


print("update data by (column name, value, id) ...")
# c.execute("UPDATE `members` SET `%s`='%s' WHERE `id`=13", ["name", "XXXXXXX"])
# c.execute("UPDATE `members` SET `name`='Gill' WHERE `id`=%s", ["13"])
# e.commit()


show_table(e, c, "members")

# ------------------------- 2020-0704
c.execute("INSERT INTO `members`(`name`,`birthday`,`address`) VALUES('Jason', '1963-07-31', 'LA')")
e.commit()

# 取得最後一筆新增資料的id
print("Last Row ID after INSERT is", c.lastrowid)


e.close()
