import pymysql
from os import system
from my_op import get_instruction, show_table, insert_data, update_data, delete_data, add_phone, delete_phone

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': None,
    'db': 'python_ai',
    'charset': 'utf8'
}
config['passwd'] = input("請輸入資料庫root密碼：")
config['port'] = int(input("請輸入資料庫的port："))
e = pymysql.connect(**config)
c = e.cursor()

system('cls')
show_table(e, c, "member")
# 取得第一個指令
ins = get_instruction()

while ins != 0:
    if ins == 1:
        system('cls')
        show_table(e, c, "member")
    elif ins == 2:
        system('cls')
        insert_data(e, c, "member")
        system('cls')
    elif ins == 3:
        system('cls')
        show_table(e, c, "member")
        update_data(e, c, "member")
    elif ins == 4:
        system('cls')
        show_table(e, c, "member")
        delete_data(e, c, "member")
        system('cls')
    elif ins == 5:
        system('cls')
        show_table(e, c, "member")
        add_phone(e, c)
        system('cls')
    elif ins == 6:
        system('cls')
        show_table(e, c, "member")
        delete_phone(e, c,)
        system('cls')

    # get the next instruction
    ins = get_instruction()
e.close()
