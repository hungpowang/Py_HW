import pymysql
from os import system
from my_operation import get_instruction, show_table, insert_data, update_data, delete_data

# my localhost
# config = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'root',
#     'passwd': None,
#     'db': 'python_ai',
#     'charset': 'utf8'
# }

# AWS
config = {
    'host': 'mysql-ai.c62pxjbypfwu.ap-northeast-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'admin',
    'passwd': 'mZVc55ItGNLA1kBfyeF5',
    'db': 'python_ai',
    'charset': 'utf8'
}
# config['passwd'] = input("請輸入資料庫root密碼：")
# config['port'] = int(input("請輸入資料庫的port："))
e = pymysql.connect(**config)
c = e.cursor()

system('clear')
show_table(e, c, "member")
# 取得第一個指令
ins = get_instruction()

while ins != 0:
    if ins == 1:
        system('clear')
        show_table(e, c, "member")
    elif ins == 2:
        system('clear')
        insert_data(e, c, "member")
        system('clear')
    elif ins == 3:
        system('clear')
        show_table(e, c, "member")
        update_data(e, c, "member")
    elif ins == 4:
        system('clear')
        show_table(e, c, "member")
        delete_data(e, c, "member")
        system('clear')

    # get the next instruction
    ins = get_instruction()
e.close()
