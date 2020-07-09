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
(4) 刪除會員資料""" )
    while True:
        try: 
            ins = int(input('指令: '))
        except ValueError:
            print("Please input an integer(0~4)")
            continue
        if -1 < ins < 5:
            break
    return ins


def show_table(conn, cur, table_name):
    '''
    以表格方式印出資料表
    '''
    # 取得table所有列
    cur.execute("SELECT * FROM `" + table_name + "`")
    rows = cur.fetchall()
    conn.commit
    col_names = ['編號', '姓名', '生日', '地址']
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
    # cur.execute("UPDATE `member` SET `name`='sdfsfd', `birthday`='9999-01-05', `address`='Boston' WHERE `id`='24'")
    conn.commit()
