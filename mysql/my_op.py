import prettytable


def get_instruction():
    '''
    Get a legal instruction number
    '''
    print("""
(0) 離開程式
(1) 顯示會員列表
(2) 新增會員資料
(3) 更新會員資料
(4) 刪除會員資料
(5) 新增會員的電話
(6) 刪除會員的電話""" )
    while True:
        try: 
            ins = int(input('指令: '))
        except ValueError:
            print("Please input an integer(0~6)")
            continue
        if -1 < ins < 7:
            break
    return ins


def show_table(conn, cur, table_name):
    '''
    以表格方式印出資料表
    '''
    # 取得table所有列
    # ("SELECT * FROM `" + table_name + "`")
    cur.execute("SELECT `a`.*,`b`.`tel` FROM `member` AS `a` LEFT JOIN `tel` AS `b` on `a`.`id`=`b`.`member_id`")
    rows = cur.fetchall()
    conn.commit
    col_names = ['編號', '姓名', '生日', '地址', '電話']
    # 用prettytable印出來
    table = prettytable.PrettyTable(col_names, encoding='utf8')
    for r in rows:
        table.add_row(list(r))
    print("TABLE:", table_name)
    print(table)


def insert_data(conn, cur, table_name):
    '''
    使用者輸入新增資料
    '''
    cur.execute("INSERT INTO `member`(`name`,`birthday`,`address`) VALUES(%(a)s,%(b)s,%(c)s)",
            {
            "a": input("請輸入會員姓名："),
            "b": input("請輸入會員生日："),
            "c": input("請輸入會員地址：")
            })
    conn.commit()


def delete_data(conn, cur, table_name):
    '''
    詢問id式刪除資料
    '''
    cur.execute("DELETE FROM `member` WHERE `id`=%s", [ input("請問你要刪除的資料編號：") ])
    conn.commit()


def update_data(conn, cur, table_name):
    id = input("選擇你要修改的資料編號:")
    name = input("請輸入會員姓名：")
    bd = input("請輸入會員生日：")
    addr = input("請輸入會員地址：")
    cur.execute("UPDATE `member` SET `name`=%s, `birthday`=%s, `address`=%s WHERE `id`=%s", [name, bd, addr, id])
    conn.commit()


def add_phone(conn, cur):
    # id = input("請選擇要添加電話的會員編號:")
    # phone = input("請輸入電話：")
    # cur.execute("UPDATE `tel` SET `tel`=%s WHERE `member_id`=%s", [phone, id])
    cur.execute("INSERT INTO `tel`(`member_id`,`tel`) VALUES(%(a)s,%(b)s)",
            {
            "a": input("請選擇要添加電話的會員編號:"),
            "b": input("請輸入電話：")
            })
    conn.commit()


def show_number_table(conn, cur):
    # 取得table所有列
    # ("SELECT * FROM `" + table_name + "`")
    id = input("請選擇要刪除電話的會員編號：")
    cur.execute("SELECT `id`,`tel` FROM `tel` WHERE `member_id`=%s", [id])
    rows = cur.fetchall()
    conn.commit
    col_names = ['編號', '電話']
    # 用prettytable印出來
    table = prettytable.PrettyTable(col_names, encoding='utf8')
    for r in rows:
        table.add_row(list(r))
    print(table)


def delete_phone(conn, cur):
    '''
    詢問式刪除電話
    '''
    show_number_table(conn, cur)
    # id = input("請選擇要刪除電話的電話編號：")
    
    cur.execute("DELETE FROM `tel` WHERE `id`=%s", [ input("請選擇要刪除電話的電話編號：") ])
    conn.commit()
